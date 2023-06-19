#program to check factorial of a number

def factorial(number):
    if number < 0:
        return "Factorial does not exist for negative numbers"
    elif number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

given = int(input("Please provide the number to check factorial: "))

print(f'Factorial of {given} is {factorial(given)}')
