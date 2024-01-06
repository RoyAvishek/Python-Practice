# Problem: Write a Python program to reverse a string.
#abc -> cba

def reverse(str):
    return str[::-1]

given = input("Please write a string to reverse: ")

print(f'Rversed string is {reverse(given)}')





def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string

# Example usage
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)