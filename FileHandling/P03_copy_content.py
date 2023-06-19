# Implement a function that copies the contents of one text file to another.

def copy_content(src_file, dest_file):
    try:
        with open(src_file, 'r') as src:
            src_file_content = src.read()
    except FileNotFoundError:
        print(f'Source file "{src_file}" not found. Please provide the correct path.')
        return

    try:
        with open(dest_file, 'w') as dest:
            dest.write(src_file_content)
    except FileNotFoundError:
        print(f'Destination file "{dest_file}" not found. Please provide the correct path.')
        return

    print(f'Contents of "{src_file}" copied to "{dest_file}" successfully.')


src_file = "FileHandling/test.txt"
dest_file = "FileHandling/test1.txt"

copy_content(src_file, dest_file)

