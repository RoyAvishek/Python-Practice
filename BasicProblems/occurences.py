# Problem: Write a Python program to count the occurrences of each word in a given sentence.

# brute force solution
# def occ_checker(sentence):
#     words = sentence.split()
#     unique_words = set(words)

#     for word in unique_words:
#         occurance = words.count(word)
#         print(f'Total occurence of {word} = {occurance}')


# given = input("Please write a sentence to check occurence of each words: ")
# occ_checker(given)


# Time optimized O(n) sol.
def occ_checker(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word, count in frequency.items():
        print(f'Total occurrence of {word} = {count}')


given = input("Please write a sentence to check the occurrence of each word: ")
occ_checker(given)