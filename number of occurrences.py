'''
Write a function that counts the number of different characters in a string. 
The character is in the ASCII code range (0 to 127, including 0 and 127), and the newline represents the end character, which is not included in the character. 
Those not within the scope will not be counted. Multiple identical characters are counted only once
For example, for the string abaca, there are three different characters a, b, and c, so the output is 3.
'''

def count_different_characters(input_string):
    unique_characters = set()

    for char in input_string:
        # Check if the character is within the ASCII range (0 to 127)
        if 0 <= ord(char) <= 127 and char != '\n':
            unique_characters.add(char)

    return len(unique_characters)

# Example usage
input_str = "abc"
result = count_different_characters(input_str)
print(result)

