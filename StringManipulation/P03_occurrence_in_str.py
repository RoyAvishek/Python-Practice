# Create a program that counts the occurrence of each character in a string.
# avishek -> a -> 1, v -> 1


def occ_checker(str):
    chars = list(str)
    unique_chars = set(chars)

    print("Occurrence of each char is")
    for char in unique_chars:
        occ = str.count(char)
        print(f'{char} - > {occ}')


given = input("Please type a string: ")
occ_checker(given)
