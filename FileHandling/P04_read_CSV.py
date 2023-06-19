# Write a program that reads a CSV file and prints specific columns.

import csv

def print_specific_columns(csv_file, columns):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header row
            
            # Find the indices of the specified columns in the header
            column_indices = [headers.index(column) for column in columns]
            
            # Print the specified columns for each row
            for row in reader:
                row_values = [row[index] for index in column_indices]
                print(*row_values)
    except FileNotFoundError:
        print(f'File "{csv_file}" not found. Please provide the correct path.')


# Example usage
csv_file = "data.csv"
columns_to_print = ['Name', 'Age', 'Country']

print_specific_columns(csv_file, columns_to_print)
