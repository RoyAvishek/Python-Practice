# Implement a program that sorts a list of dictionaries based on a specific key.

def sort_list_of_dictionaries(lst, key):
    sorted_list = sorted(lst, key=lambda x: x[key])
    return sorted_list


# Example usage
data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20}
]

sorted_data = sort_list_of_dictionaries(data, "age")
print(sorted_data)
