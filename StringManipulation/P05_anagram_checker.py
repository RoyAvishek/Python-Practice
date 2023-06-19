# Implement a function that checks if two strings are anagrams of each other.
# Anagram -> heart : earth

def anagram_checker(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        return "Anagram"
    else:
        return "Not Anagram"
    

given1 = input("Please type first string: ")
given2 = input("Please type second string: ")

print(f'Given strings are {anagram_checker(given1, given2)}')