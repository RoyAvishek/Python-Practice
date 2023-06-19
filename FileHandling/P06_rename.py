# Create a program that renames a file.

import os

def rename_file(file_path, new_name):
    try:
        # Split the file path and name
        dir_name, old_name = os.path.split(file_path)

        # Construct the new file path with the new name
        new_file_path = os.path.join(dir_name, new_name)

        # Rename the file
        os.rename(file_path, new_file_path)

        print(f"File '{file_path}' renamed to '{new_file_path}'")
    except FileNotFoundError:
        print('File not found. Please provide a valid file path.')


file_path = "path/to/your/file.txt"
new_name = "new_file_name.txt"

rename_file(file_path, new_name)
