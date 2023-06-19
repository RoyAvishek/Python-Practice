# Implement a function that merges two dictionaries into a new dictionary.

def merge_dict(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict


dict1 = {
    "Name" : "Avishek"
}

dict2 = {
    "Age" : "26"
}

print(f'{merge_dict(dict1,dict2)}')