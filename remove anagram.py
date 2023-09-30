'''
Given an array of words, delete the words which is anagram of any of the previous ones, return a sorted list of words
'''

def remove_anagram(words):
    unique = {}

    for s in words:
        sorted_s = ''.join(sorted(s))

        if sorted_s not in unique:
            unique[sorted_s] = s
        
    return sorted(unique.values())


# test
words = ["anagrams", "coed", "aaagmnrs", "anagrams", "doce"]
print(remove_anagram(words))

