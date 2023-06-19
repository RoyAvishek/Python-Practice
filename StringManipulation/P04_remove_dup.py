# Write a function that removes all duplicates from a string and returns the result.
# aavvvishek -> avishek

def remove_dup(str):
    uniq_chars = []
    
    for char in str:
        if char not in uniq_chars:
            uniq_chars.append(char)
    result = ''.join(uniq_chars)
    print(result)


given = input("Please type a string: ")
remove_dup(given)