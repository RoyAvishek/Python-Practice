# Write a program that reverses a given list without using built-in functions.

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        # Swap elements at start and end indices
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst


# Example usage
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list)