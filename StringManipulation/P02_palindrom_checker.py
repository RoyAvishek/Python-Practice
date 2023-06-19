# Implement a function that checks if a string is a palindrome.
# cat -> not palindrom : bob -> palindrom

def palindrom_checker(str):
    if str == str[::-1]:
        return "Palindrom"
    return "not Palindrom"

given = input("Please type a string to check if it is palindrom or not: ")
print(f'{given} is {palindrom_checker(given)}')