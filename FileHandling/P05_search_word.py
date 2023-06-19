# Create a program that searches for a specific word in a text file and prints the line number(s) where it occurs.

def search_word(file_path, word):
    try:
        with open(file_path, 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if word in line:
                    print(f"Word '{word}' found at line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print('File not found. Please provide a valid file path.')


file_path = "path/to/your/file.txt"
search_word(file_path, "specific")
