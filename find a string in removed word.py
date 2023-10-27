'''
How many words after removing one letter will contain a given string
'''

def letter_remove(w, s):
    count = 0
    removed = [w[:i] + w[i+1:] for i in range(len(w))]
    for r in removed:
        if s in r:
            count += 1
    return count

# test
word = 'example'
# check = 'ex'
print(letter_remove(word, check))

