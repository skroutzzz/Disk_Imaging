import sys
import os
import pytsk3
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeView, QVBoxLayout, QTableView, QTextEdit, QMessageBox
from PySide6.QtCore import Slot, Qt, QModelIndex, QThread, Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.MainWindow import Ui_MainWindow
from runCaseInfoWindow import CaseInfoWindow
from runNewHostWindow import NewHostWindow


def get_partition_offset(image_path):
    try:
        result = subprocess.run(['mmls', image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error running mmls: {result.stderr}")
            return None
        print("mmls output:\n", result.stdout)
        lines = result.stdout.splitlines()
        for line in lines:
            if 'Win95 FAT32' in line:
                parts = line.split()
                if len(parts) > 3 and parts[2].isdigit():
                    offset = int(parts[2]) * 512
                    return offset
    except Exception as e:
        print(f"Error: {e}")
        return None


def list_files(fs_info, path='/'):
    directory = fs_info.open_dir(path=path)
    files = []
    for entry in directory:
        if entry.info.name.name.decode('utf-8') in ['.', '..']:
            continue
        file_info = {
            'name': entry.info.name.name.decode('utf-8'),
            'type': entry.info.meta.type if entry.info.meta else 'Unknown',
            'size': entry.info.meta.size if entry.info.meta else 'Unknown',
            'created': entry.info.meta.crtime if entry.info.meta else 'Unknown',
            'modified': entry.info.meta.mtime if entry.info.meta else 'Unknown',
            'path': f"{path}/{entry.info.name.name.decode('utf-8')}"
        }
        if entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
            file_info['children'] = list_files(fs_info, file_info['path'])
        files.append(file_info)
    return files


def update_treeview(treeview, files, root_name):
    model = treeview.model()
    if model is None:
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Name"])
        treeview.setModel(model)

    root_item = QStandardItem(root_name)
    root_item.setFlags(root_item.flags() & ~Qt.ItemIsEditable)

    def add_items(parent, file_info):
        item_name = QStandardItem(file_info['name'])
        item_name.setFlags(item_name.flags() & ~Qt.ItemIsEditable)
        parent.appendRow(item_name)
        if file_info['type'] == pytsk3.TSK_FS_META_TYPE_DIR:
            for child in file_info.get('children', []):
                add_items(item_name, child)

    for file in files:
        add_items(root_item, file)

    model.appendRow(root_item)
    treeview.setAlternatingRowColors(True)
    treeview.setSelectionBehavior(QTreeView.SelectRows)
    treeview.setUniformRowHeights(True)
    treeview.expandAll()


def update_tableview(tableview, files):
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Name", "Type", "Size", "Created", "Modified"])

    for file_info in files:
        item_name = QStandardItem(file_info['name'])
        item_name.setFlags(item_name.flags() & ~Qt.ItemIsEditable)
        item_type = QStandardItem('Directory' if file_info['type'] == pytsk3.TSK_FS_META_TYPE_DIR else 'File')
        item_type.setFlags(item_type.flags() & ~Qt.ItemIsEditable)
        item_size = QStandardItem(str(file_info['size']))
        item_size.setFlags(item_size.flags() & ~Qt.ItemIsEditable)
        item_created = QStandardItem(str(file_info['created']))
        item_created.setFlags(item_created.flags() & ~Qt.ItemIsEditable)
        item_modified = QStandardItem(str(file_info['modified']))
        item_modified.setFlags(item_modified.flags() & ~Qt.ItemIsEditable)

        model.appendRow([item_name, item_type, item_size, item_created, item_modified])

    tableview.setModel(model)
    tableview.setAlternatingRowColors(True)
    tableview.setSelectionBehavior(QTableView.SelectRows)
    tableview.resizeColumnsToContents()
    tableview.resizeRowsToContents()


def process_image(image_path):
    image_path = os.path.expanduser(image_path)

    if not os.path.exists(image_path):
        print(f"Error: File does not exist: {image_path}")
        return None
    elif not os.access(image_path, os.R_OK):
        print(f"Error: File is not readable: {image_path}")
        return None

    partition_offset = get_partition_offset(image_path)
    if partition_offset is None:
        print("Could not determine partition offset.")
        return None

    try:
        img_info = pytsk3.Img_Info(image_path)
        fs_info = pytsk3.FS_Info(img_info, offset=partition_offset)
        files = list_files(fs_info)
        return files, partition_offset
    except OSError as e:
        print(f"Error opening image: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None


class HexWorker(QThread):
    hex_ready = Signal(str)

    def __init__(self, image_path, partition_offset, file_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.partition_offset = partition_offset
        self.file_path = file_path

    def run(self):
        hex_content = self.get_file_hex_content(self.image_path, self.partition_offset, self.file_path)
        self.hex_ready.emit(hex_content)

    def get_file_hex_content(self, image_path, partition_offset, file_path):
        try:
            img_info = pytsk3.Img_Info(image_path)
            fs_info = pytsk3.FS_Info(img_info, offset=partition_offset)
            file_obj = fs_info.open(file_path)
            file_data = file_obj.read_random(0, min(file_obj.info.meta.size, 1024))
            hex_content = file_data.hex()
            formatted_hex = '\n'.join(hex_content[i:i + 32] for i in range(0, len(hex_content), 32))
            return formatted_hex
        except Exception as e:
            print(f"Error reading file: {e}")
            return None


class TextWorker(QThread):
    text_ready = Signal(str)

    def __init__(self, image_path, partition_offset, file_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.partition_offset = partition_offset
        self.file_path = file_path

    def run(self):
        text_content = self.get_file_text_content(self.image_path, self.partition_offset, self.file_path)
        self.text_ready.emit(text_content)

    def get_file_text_content(self, image_path, partition_offset, file_path):
        try:
            img_info = pytsk3.Img_Info(image_path)
            fs_info = pytsk3.FS_Info(img_info, offset=partition_offset)
            file_obj = fs_info.open(file_path)
            file_data = file_obj.read_random(0, min(file_obj.info.meta.size, 1024))
            text_content = file_data.decode(errors='replace').replace('\x00', '\uFFFD')
            return text_content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.mw_newCaseButton.clicked.connect(self.open_caseInfoWindow)
        self.mw_addDataSourceButton.clicked.connect(self.open_newHostWindow)
        self.mw_openCaseButton.clicked.connect(self.open_image)
        self.mw_hexButton.clicked.connect(self.show_hex_content)
        self.mw_textButton.clicked.connect(self.show_text_content)

        self.mw_treeView.setHeaderHidden(True)
        self.mw_treeView.clicked.connect(self.on_treeview_clicked)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Forensic Image", "", "Forensic Images (*.dd *.img)")
        if file_path:
            self.add_image_to_treeview(file_path)

    def add_image_to_treeview(self, file_path):
        image_name = os.path.basename(file_path)
        self.image_path = file_path
        files, partition_offset = process_image(file_path)
        if files:
            self.partition_offset = partition_offset
            update_treeview(self.mw_treeView, files, image_name)
            self.files = files
            print("Loaded files structure:")
            print(self.files)

    @Slot(QModelIndex)
    def on_treeview_clicked(self, index):
        item = self.mw_treeView.model().itemFromIndex(index)
        self.current_path = self.get_full_path(item)
        print(f"Tree view clicked, current path: {self.current_path}")
        dir_info = self.get_directory_info(self.current_path)
        if dir_info is not None:
            print(f"Directory info found for path: {self.current_path}")
            update_tableview(self.mw_tableView, dir_info)
        else:
            print(f"No directory info found for path: {self.current_path}")

    def get_full_path(self, item):
        path = []
        while item is not None:
            path.insert(0, item.text())
            item = item.parent()
        full_path = '/' + '/'.join(path[1:])
        print(f"Full path resolved: {full_path}")
        return full_path

    def get_directory_info(self, path):
        def find_directory(files, path_parts):
            print(f"Finding directory in files: {files} with path_parts: {path_parts}")
            if not path_parts:
                return files
            for file_info in files:
                print(f"Checking file info: {file_info['name']} against {path_parts[0]}")
                if file_info['name'] == path_parts[0]:
                    if len(path_parts) == 1:
                        print(f"Found directory: {file_info['name']} with children: {file_info.get('children', [])}")
                        return file_info.get('children', [])
                    elif 'children' in file_info:
                        return find_directory(file_info['children'], path_parts[1:])
            return None

        path_parts = path.strip('/').split('/')
        return find_directory(self.files, path_parts)

    @Slot()
    def open_caseInfoWindow(self):
        self.caseWindow = CaseInfoWindow()
        self.caseWindow.show()

    @Slot()
    def open_newHostWindow(self):
        self.newHostWindow = NewHostWindow()
        self.newHostWindow.show()

    @Slot()
    def show_hex_content(self):
        selected_indexes = self.mw_tableView.selectionModel().selectedRows()
        if not selected_indexes:
            return

        selected_index = selected_indexes[0]
        item_name = self.mw_tableView.model().item(selected_index.row(), 0).text()
        dir_info = self.get_directory_info(self.current_path)
        for file_info in dir_info:
            if file_info['name'] == item_name:
                file_path = file_info['path']
                break
        else:
            return

        self.hex_worker = HexWorker(self.image_path, self.partition_offset, file_path)
        self.hex_worker.hex_ready.connect(self.display_hex_content)
        self.hex_worker.start()

    @Slot(str)
    def display_hex_content(self, hex_content):
        if hex_content:
            self.mw_textEdit.setPlainText(hex_content)
        else:
            QMessageBox.warning(self, "Error", "Could not read file content in hex.")

    @Slot()
    def show_text_content(self):
        selected_indexes = self.mw_tableView.selectionModel().selectedRows()
        if not selected_indexes:
            return

        selected_index = selected_indexes[0]
        item_name = self.mw_tableView.model().item(selected_index.row(), 0).text()
        dir_info = self.get_directory_info(self.current_path)
        for file_info in dir_info:
            if file_info['name'] == item_name:
                file_path = file_info['path']
                break
        else:
            return

        self.text_worker = TextWorker(self.image_path, self.partition_offset, file_path)
        self.text_worker.text_ready.connect(self.display_text_content)
        self.text_worker.start()

    @Slot(str)
    def display_text_content(self, text_content):
        if text_content:
            self.mw_textEdit.setPlainText(text_content)
        else:
            QMessageBox.warning(self, "Error", "Could not read file content in text.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
