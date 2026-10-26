# Python File Manager 📁

A small Python project built as part of my **FDE Bootcamp** to practise file handling, exception handling, and object-oriented programming.

### Features

- Create project structure with minimal efforts.
- Read and write text files.
- List files in a directory.
- Sort filenames and convert them to uppercase.
- Find report files and analyse filename lengths.
- Practise list and dictionary comprehensions and built-in functions.
- Handle common file-related errors.

### Getting Started

**Requirements:** Python 3.x

1. Clone this repository.
2. Navigate to the project directory.
3. Run the main Python file:

```bash
python run.py
```

### Usage Example

```python
from file_manager import FileManager

# Create a file manager for the data directory
manager = FileManager("data")

# Save some text
manager.write_file("report.txt", "Hello! This is my first report.")

# Read the saved file
print(manager.read_file("report.txt"))

# List files in the directory
print(manager.list_files())

# Get filenames and their character counts
print(manager.get_lengths_dict())

# Check whether any report files exist
print(manager.has_any_reports())
```

### Concepts Practised

Python OOP (`class`, `self`, constructors, and methods), the `os` module, file paths, exception handling, list and dictionary comprehensions, and built-in functions such as `any()`, `all()`, `sorted()`, `map()`, `filter()`, and `zip()`.

### Purpose

This project is part of my journey to strengthen my Python fundamentals through practical coding and hands-on learning. More improvements will follow as I continue learning.
