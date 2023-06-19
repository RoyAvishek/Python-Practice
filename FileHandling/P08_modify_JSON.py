# Write a program that reads a JSON file, modifies its contents, and saves it back to the file.

import json

def modify_json_file(file_path, key, new_value):
    try:
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Modify the value of the specified key
        data[key] = new_value

        # Write the modified data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"JSON file '{file_path}' modified successfully.")
    except FileNotFoundError:
        print('File not found. Please provide a valid file path.')
    except json.JSONDecodeError:
        print('Invalid JSON format. Please provide a valid JSON file.')

file_path = "path/to/your/file.json"
key = "name"
new_value = "John Doe"

modify_json_file(file_path, key, new_value)
