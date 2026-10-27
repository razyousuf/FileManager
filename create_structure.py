
import os

from structure import DirectoryManager
from statics import REQUIRED_FOLDERS, REQUIRED_FILES


class CreateStructure:
    def __init__(self, root_dir=None):
        # Use this script's directory by default, not the launch directory.
        if root_dir is None:
            root_dir = os.path.dirname(os.path.abspath(__file__))

        self.root_dir = os.path.abspath(root_dir)
        self.dirmanager = DirectoryManager(self.root_dir)

    def create_folders(self):
        """Create all required folders without disturbing existing ones."""
        for folder in REQUIRED_FOLDERS:
            folder_path = os.path.join(self.root_dir, folder)

            if not os.path.isdir(folder_path):
                print(f"Creating folder: {folder}")
                self.dirmanager.create_directory(folder)
            else:
                print(f"Folder already exists: {folder}")

    def create_files(self):
        """Create required files without overwriting existing files."""
        for file_info in REQUIRED_FILES:
            sub_folder = file_info["sub_folder"]
            file_name = file_info["file_name"]
            content = file_info["content"]

            file_path = os.path.join(
                self.root_dir,
                sub_folder,
                file_name,
            )

            if os.path.isfile(file_path):
                print(
                    f"File already exists: {file_name} "
                    f"in folder: {sub_folder or '.'}"
                )
                continue

            print(
                f"Creating file: {file_name} "
                f"in folder: {sub_folder or '.'}"
            )

            self.dirmanager.create_file(
                sub_folder=sub_folder,
                file_name=file_name,
                content=content,
            )

    def create_structure(self):
        """Create the complete initial project structure."""
        self.create_folders()
        self.create_files()


# if __name__ == "__main__":
#     creator = CreateStructure()
#     creator.create_structure()
