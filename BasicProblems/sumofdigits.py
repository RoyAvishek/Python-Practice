# Problem: Write a Python program to find the sum of digits of a number.

def sum_digits(num):
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    return sum

given = int(input("Please give the number to sum the digits: "))
print(f'sum of the digits of the given number is {sum_digits(given)}')