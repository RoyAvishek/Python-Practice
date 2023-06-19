# Write a function that removes duplicate elements from a list and returns a new list.

def remove_duplicates(lst):
    unique_list = []

    for element in lst:
        if element not in unique_list:
            unique_list.append(element)

    return unique_list


# Example usage
data = [1, 2, 3, 2, 4, 1, 5, 4]
result = remove_duplicates(data)
print(result)
