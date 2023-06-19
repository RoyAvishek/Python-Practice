# Implement a program that finds the longest common prefix among a list of strings.
# flower, flow, flag -> fl

def longest_common_prefix(strings):
    if not strings:
        return ''

    prefix = strings[0]
    for string in strings[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ''
    
    return prefix


words = ['flower', 'flow', 'flight']
result = longest_common_prefix(words)
print(f'Longest common prefix is {result}')







