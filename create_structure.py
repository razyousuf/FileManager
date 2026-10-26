import os
from structure import create_directory, create_file

# Define portable root directory
ROOT_DIR = os.getcwd()

# 1. Automate Folder Creation
def create_folders:
    # We create a dedicated 'documents' folder for the office files, and 'src' for code logic
    required_folders = [
        "src",
        "data",
        "reports"
    ]

    for folder in required_folders:
        if not os.path.exists(os.path.join(ROOT_DIR, folder)):
            print(f"Creating folder: {folder}")
            create_directory(ROOT_DIR, folder)
        else:
            print(f"Folder already exists: {folder}")
    

# 2. Automate File Creation
# Leave sub_folder as "" if you want the file written directly to the root directory
required_files = [
    {
        "sub_folder": "", 
        "file_name": "run.py", 
        "content": """# This is the main entry point for the application"""
    },
    {
        "sub_folder": "src", 
        "file_name": "__init__.py", 
        "content": """# Marks this directory as a Python package"""
    },
     {
        "sub_folder": "src", 
        "file_name": "file_manager.py", 
        "content": """# Manages text documents within a dedicated data workspace."""
     },
]

# Create all files in a single, simple loop
for file_info in required_files:
    if not os.path.exists(os.path.join(ROOT_DIR, file_info["sub_folder"], file_info["file_name"])):
        print(f"Creating file: {file_info['file_name']} in folder: {file_info['sub_folder']}")
        create_file(
            base_dir=ROOT_DIR,
            sub_folder=file_info["sub_folder"],
            file_name=file_info["file_name"],
            content=file_info["content"]
        )
    else:
        print(f"File already exists: {file_info['file_name']} in folder: {file_info['sub_folder']}")