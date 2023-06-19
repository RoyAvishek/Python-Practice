# Create a program that capitalizes the first letter of each word in a sentence.
# My name is avishek -> My Name Is Avishek

def capitalize_first_char(str):
    return str.title()
    # words = str.split()
    
    # for word in words:
    #     word[0] = word[0].upper()

given = input("Please type a sentance: ")
print(f'{capitalize_first_char(given)}')


# def capitalize_sentence(sentence):
#     words = sentence.split()
#     capitalized_words = []

#     for word in words:
#         capitalized_word = word[0].upper() + word[1:]
#         capitalized_words.append(capitalized_word)

#     capitalized_sentence = ' '.join(capitalized_words)
#     return capitalized_sentence

# sentence = "hello world! how are you?"
# result = capitalize_sentence(sentence)
# print(result)