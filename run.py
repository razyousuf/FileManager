# This is the main entry point for the application
import os
from 
from src.file_manager import FileManager

if __name__ == '__main__':
    try:
        
        
        # Initialise the system using the 'data' folder
        manager = FileManager(storage_dir='data')
        
        # 1. Create and Save Files
        manager.write_file('notes.txt', 'Learning Python file handling.')
        manager.write_file('report.txt', 'Quarterly report content.')
        
        # 2. Read saved information
        print(f'\nFile content: {manager.read_file("notes.txt")}')
        
        # 3. Directory Context & Listing
        # Replaces absolute local paths with clean trailing folder representations
        cwd = os.getcwd().replace('\\', '/').split('/')[-1]
        print(f'\nCurrent working directory: .../{cwd}')
        print(f'Managed directory: .../{cwd}/{manager.storage_dir}')
        
        contents = manager.list_files()
        print(f'Directory contents: {contents}')
        
        print('\nText files:')
        for file in contents:
            print(file)
            
        # 4. Deep Analysis using Comprehensions & Built-ins
        print('\nFile analysis:')
        for i, file in enumerate(contents, 1):
            print(f'{i}. {file}')
            
        # Complex Comprehension Layouts requested by target output
        print(f'\nDictionary of filename lengths: {manager.get_lengths_dict()}')
        print(f'Sorted files by name length: {manager.get_sorted_by_length()}')
        print(f'Sorted files by name length: {manager.get_sorted_lambda()}')        
        print(f'Uppercase filenames: {manager.get_uppercase_names()}')
        print(f'Report files: {manager.get_report_files()}')
        print(f'Any report files? {manager.has_any_reports()}')
        print(f'Check all text files: {manager.get_txt_files()}')
        print(f'Using Lambda, check all text files: {manager.get_txt_files_lambda()}')
        print(f'Filename-length pairs: {manager.get_name_length_pairs()}')
        print(f'Filename-length pairs using zip: {manager.get_filename_length_pairs_zip()}')
        print(f'Filename lengths using map(): {manager.get_filename_lengths()}')
        print(f'Delete the file: {manager.delete_file("notes.txt")}')
        # 5. Handle missing file error explicitly
        print('\nTesting a missing file:')
        
        print(f'\nFile content: {manager.read_file("missing.txt")}')
            
        # 6. Validate a filename using the static method
        print(f'\nFile name validation result: {manager.is_valid_filename("report.txt")}')
    
        # 7. Demonstrate the use of a class method to create an instance from a configuration dictionary
        config = {'storage_dir': 'reports'}
        manager2 = FileManager.from_config(config)
        print(f'\nNew FileManager instance created with storage directory: {manager2.storage_dir}')
        manager2.write_file('new_report.txt', 'This is a new report file created in the reports directory.')
        print(f'Contents: {manager2.read_file("new_report.txt")}')
        print(f'Directory content: {manager2.list_files()}')
        
    except Exception as e:
        print(f'An unexpected error occurred: {e}')        
        