'''
Given an array of words, delete the words which is anagram of only the previous one, return a sorted list of words
'''

def remove_anagram(words):
    unique = []
    prev_word = ''

    for s in words:
        sorted_s = ''.join(sorted(s))

        if sorted_s != ''.join(sorted(prev_word)):
            unique.append(s)

        prev_word = s

    return unique


# test
words = ["anagrams", "code", "aaagmnrs", "anagrams", "doec", "doce"]
print(remove_anagram(words))
