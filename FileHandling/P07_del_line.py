# Implement a function that deletes a specific line from a text file.

def delete_line(file_path, line_number):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Delete the specified line from the list
        if line_number >= 1 and line_number <= len(lines):
            del lines[line_number - 1]

        # Write the updated contents back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Line {line_number} deleted from file '{file_path}'")
    except FileNotFoundError:
        print('File not found. Please provide a valid file path.')


file_path = "path/to/your/file.txt"
line_number = 3

delete_line(file_path, line_number)
