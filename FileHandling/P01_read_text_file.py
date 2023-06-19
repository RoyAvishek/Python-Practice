# Write a program that reads a text file and prints its contents.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("Error reading file!")

# Example usage
file_path = 'FileHandling/test.txt'
read_file(file_path)