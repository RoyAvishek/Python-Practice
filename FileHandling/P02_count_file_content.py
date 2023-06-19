# Create a program that counts the number of lines, words, and characters in a text file.

def count_lines_words_chars(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count, word_count, char_count = 0, 0, 0
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                for word in words:
                    char_count += len(word)
        return line_count, word_count, char_count           
    except FileNotFoundError:
        print('File not Exist. Please give correct path.')
        
        
file_to_check = "FileHandling/test.txt"
line_count, word_count, char_count = count_lines_words_chars(file_to_check)

print(f'Line count: {line_count}, Word count: {word_count}, Char count: {char_count}')

