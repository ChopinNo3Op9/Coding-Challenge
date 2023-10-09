'''
Reverse the order of the words.
'''

# def reverse(words):
#     word = "".join(words)
#     word_list = word.split(" ")[::-1]
#     reverse_word = " ".join(word_list)
#     reverse_list = [s for s in reverse_word]
#     return reverse_list

def reverse(words):
    def reverse_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            

    words.reverse()
    start = 0
    for end in range(len(words)):
        if words[end] == ' ':
            reverse_word(words, start, end - 1)
            start = end + 1
    
    reverse_word(words, start, len(words) - 1)  # the last word
    
    return words

# test
# string = ["a"]
string = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(reverse(string))

