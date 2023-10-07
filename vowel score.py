'''
The score of a single word is  if the word contains an even number of vowels. Otherwise, the score of this word is . 
The score for the whole list of words is the sum of scores of all words in the list.
'''

def is_vowel(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return word in vowel

def vowel_score(s):
    score = 0
    for word in s:
        count = 0
        for letter in word:
            if is_vowel(letter):
                count += 1
        if count % 2 == 0:
            score += 2
        else:
            score += 1
    return score


# test
input = ['hacker', 'book', 'app']
print(vowel_score(input))
