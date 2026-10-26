import os

def create_directory(base_dir, sub_path):
    """Creates a sub-directory inside a base directory."""
    target_path = os.path.join(base_dir, sub_path)
    os.makedirs(target_path, exist_ok=True)
    return target_path

def create_file(base_dir, sub_folder, file_name, content = ""):
    """Creates a file cleanly within a specified sub-folder configuration."""
    full_path = os.path.join(base_dir, sub_folder, file_name)
    
    # Ensure parent directory structure exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


         
# # Call the function by passing the parent directory and file metadata
# create_file(root_dir, "simple_file.txt", "This is a simple file created in the root directory.")

# # Call the function by securely joining the root path with the subfolder
# create_file(os.path.join(root_dir, "data"), "subfolder_file1.txt", "Created using os.path.join")

# # yet another way, but not that secure, as it relies on string concatenation:
# create_file(f"{root_dir}/data", "subfolder_file2.txt", "Created using string concatenation")

