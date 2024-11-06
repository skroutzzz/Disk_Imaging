from cx_Freeze import setup, Executable
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'Code'))

base_path = os.path.dirname(os.path.abspath(__file__))

build_exe_options = {
    "packages":["hashlib"],
    "includes":["case_info", "runCaseInfoWindow", "runIngestModuleWindow", "runNewTypeWindow", "runProgressWindow", "runSelectDataWindow"],
    "include_files":[
        (os.path.join(base_path, "Code"), "Code"),
        (os.path.join(base_path, "UI"), "UI")

        
    ],

}

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name = "DiskImagingApp",
    version="1.0",
    description="Disk Imaging GUI Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("Code/runMainWindow.py", base=base)]
)