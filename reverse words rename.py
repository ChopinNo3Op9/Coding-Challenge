'''
Reverse the order of the words.
'''

def reverse(words):
    line = words.strip()
    reverse_word = line[::-1]
    
    return reverse_word

# test
string = 'I am a student'
print(reverse(string))

