# Create a function that finds and replaces all occurrences of a specified word in a string.

# def remove_occ(str, remove):
#     words = str.split()

#     for word in words:
#         if remove == word:
#             words.remove(remove)

#     return ' '.join(words)

# sentence= "My name is avishek roy is my name"
# print(remove_occ(sentence, "is"))


def remove_occ(string, word):
    return string.replace(word, '')

sentence = "My name is avishek roy is my name"
result = remove_occ(sentence, "is")
print(result)