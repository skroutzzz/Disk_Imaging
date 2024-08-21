class CaseInfo:
    def __init__(self):
        self.case_name = ""
        self.base_directory = ""
        self.case_number = ""
        self.examiner_name = ""
        self.examiner_phone = ""
        self.examiner_email = ""
        self.notes = ""
        self.disk_type = ""
        self.source_disk = ""
        self.hash_algorithms = {
            "md5": False,
            "sha256": False,
            "verification": False
        }

    def validate_case_info(self):
        print("Validating Case info...")
        if not self.case_name:
             print("Case Name missing")
             raise ValueError("Case Name is required")
        if not self.base_directory: 
            print("Base directory missing")
            raise ValueError("Base Directory is required")
        print("Validation passed")
            

    def set_disk_type(self, disk_type):
        self.disk_type = disk_type

    def set_hash_algorithms(self, md5=False, sha256=False, verification=False):
        self.hash_algorithms["md5"] = md5
        self.hash_algorithms["sha256"] = sha256
        self.hash_algorithms["verification"] = verification

    def set_source_disk(self, disk):
        print(f"Inside set source disk, received: {disk}")
        self.source_disk = disk

