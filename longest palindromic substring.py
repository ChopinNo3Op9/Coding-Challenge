'''
Find the longest back substring
'''

def longest_palindrome_substring(s):
    n = len(s)
    res = 0

    for i in range(n):
        # extend the search one position further back each time
        back = max(0, i - res - 1)

        temp = s[back:i + 1]
        if temp == temp[::-1]:
            res = max(res, len(temp))
        elif temp[1:] == temp[1:][::-1]:
            res = max(res, len(temp) - 1)

    return res

# Example usage
# input_str = 'ABBA'
input_str = '12HHHHA'
result = longest_palindrome_substring(input_str)
print(result)
