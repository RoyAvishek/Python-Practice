# Write a program that counts the frequency of each element in a list and stores it in a dictionary.

def count_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency


# Example usage
data = [1, 2, 3, 2, 1, 3, 1, 2, 3, 4, 4, 4]
frequency = count_frequency(data)
print(frequency)
