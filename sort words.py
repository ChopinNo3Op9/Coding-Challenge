'''
Sort input words alphabetically
'''

def wordssort(words):
    words.sort()
    return [w for w in words]

# test
strings = ["cap", "to", "cat", "card", "two", "too", "up", "boat", "boot"]
print(wordssort(strings))