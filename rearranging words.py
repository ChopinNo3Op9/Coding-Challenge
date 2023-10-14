'''
Given a word, permutate all of anagram alphabatically, and return the next word of it.
'''

from itertools import permutations

def rearrange (word):
    permuted_words = [''.join(p) for p in permutations(word)]
    unique_permutations = sorted(set(permuted_words))
    
    if unique_permutations[-1] == word:
        return("no answer")
    else:
        return(unique_permutations[unique_permutations.index(word) + 1])

# test
word = "cbaa"
# word = "baca"
print(rearrange(word))
