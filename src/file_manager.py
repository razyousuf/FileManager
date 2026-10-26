
import os


# Manages text files and provides basic filename analysis.
class FileManager:

    def __init__(self, storage_dir='data'):
        # Store the directory where files will be saved and read.
        self.storage_dir = storage_dir

    def write_file(self, filename, content):
        # Save text to a file; create it if missing or replace its contents if it exists.
        try:
            path = os.path.join(self.storage_dir, filename)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'File saved successfully: {filename}')

        # Report file-related errors instead of stopping the program.
        except OSError as e:
            print(f'Error saving file {filename}: {e}')

    def read_file(self, filename):
        # Build the path and check whether the file exists before opening it.
        path = os.path.join(self.storage_dir, filename)

        if not os.path.exists(path):
            print(f'Error: {filename} does not exist.')
            return None

        # Read the saved text and return it to the caller.
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()

        # Return None if the file cannot be read.
        except OSError as e:
            print(f'Error reading file: {e}')
            return None

    def list_files(self):
        # Return directory entries in alphabetical order.
        return sorted(os.listdir(self.storage_dir))

    # Return a dictionary mapping each filename to its character count.
    def get_lengths_dict(self):
        return {f: len(f) for f in self.list_files()}

    # Sort filenames from shortest to longest using their lengths.
    def get_sorted_by_length(self):
        return sorted(self.list_files(), key=len)

    # Return uppercase versions of filenames without changing the actual files.
    def get_uppercase_names(self):
        return [f.upper() for f in self.list_files()]

    # Return filenames containing 'report' (case-sensitive).
    def get_report_files(self):
        return [f for f in self.list_files() if 'report' in f]

    # Return True if at least one filename contains 'report'; otherwise False.
    def has_any_reports(self):
        return any('report' in f for f in self.list_files())

    # Return True if every directory entry ends in '.txt'; an empty list also returns True.
    def are_all_txt(self):
        return all(f.endswith('.txt') for f in self.list_files())

    # Return a list of tuples, each containing a filename and its character count.
    def get_name_length_pairs(self):
        return [(f, len(f)) for f in self.list_files()]

    #------------------------------------------------------------------------------------#
    # Class method: Use it when a method needs to work with the class itself, rather than a particular object's data.
    @classmethod
    def from_config(cls, config):
        """Create a FileManager using a configuration dictionary."""
        return cls(config.get('storage_dir', 'data'))
    
    # Static method: Use it when a method does not need to access any instance or class data. Validating input, converting units, or checking whether a supplied value meets a rule associated with the class.
    @staticmethod
    def is_valid_filename(filename):
        """Check whether a filename has a valid basic format."""
        return (
            bool(filename)
            and os.path.basename(filename) == filename
            and filename.endswith('.txt')
        )