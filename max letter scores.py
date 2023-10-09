'''
Given a string that consists of only lowercase letters, define the "beauty" of the string as the sum of the "beauty" of all its letters. 
Each letter is assigned a "beauty rating" ranging from 1 to 26. No two different letters have the same "beauty".
Given multiple strings, calculate the maximum possible "beauty" of each string.
'''

def beauty(word):
    d = {}
    word_list = [s for s in word]
    for w in word_list:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    score = 0
    add = 26
    for key, value in sorted_d.items():
        score += value*add
        add -= 1
    return score
    

# test
# a = 'lisi'
a = 'zhangsan'
print(beauty(a))
