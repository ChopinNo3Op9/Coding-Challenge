'''
Count the occurrences of each word in a list of words. 
'''

def count_word_occurrences(word_list):
    word_count = {} 
  
    for word in word_list:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    
    return word_count

# test
words = ["bcdef", "abcdefg", "bcde", "bcdef"]
word_occurrences = count_word_occurrences(words)
for word in word_occurrences:
    print(word_occurrences.get(word, 0), end = ' ')  # 0 default value that will be returned if the word is not found in the dictionary.