import os
class DirectoryManager:
    def __init__(self, base_dir):
        # Store the root directory managed by this object.
        self.base_dir = base_dir

    def create_directory(self, sub_path):
        """Create a subdirectory inside the managed base directory."""
        target_path = os.path.join(self.base_dir, sub_path)
        os.makedirs(target_path, exist_ok=True)
        return target_path

    def create_file(self, sub_folder, file_name, content=""):
        """Create a file inside a subfolder of the managed directory."""
        folder_path = os.path.join(self.base_dir, sub_folder)
        os.makedirs(folder_path, exist_ok=True)

        full_path = os.path.join(folder_path, file_name)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return full_path