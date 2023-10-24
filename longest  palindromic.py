'''
Longest palindromic substring.
'''

def longestPalindrome(s):
    max_len = 1
    max_str = s[0]
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j] == s[i:j][::-1] and j - i + 1 > max_len:
                max_str = s[i:j]
                max_len = j - i + 1
    return max_str



# test
# string = "babad"
string = "cbbd"
print(longestPalindrome(string))

