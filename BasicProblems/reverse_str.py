# Problem: Write a Python program to reverse a string.
#abc -> cba

def reverse(str):
    return str[::-1]

given = input("Please write a string to reverse: ")

print(f'Rversed string is {reverse(given)}')