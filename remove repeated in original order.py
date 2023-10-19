'''
Given an array Q containing repeated numbers, 
the range of numbers in the array (0.9) requires that the relative positions of the resulting array composition remain unchanged after removing the repeated numbers.
'''

def process_input_string(input_str):
    s = input_str[1:-1].replace(',', '')

    if not s:
        return '[]'
    else:
        res = s[0]

        for i in range(1, len(s)):
            if s[i] not in res:
                res += s[i]
            else:
                t = res.index(s[i])
                if t + 1 < len(res) and res[t] < res[t + 1]:
                    res = res[:t] + res[t + 1:]
                    res += s[i]

        res = str(list(res)).replace("'", "").replace(" ", "")
        return res

# Example usage:
# input_str = '1,2,9,1,2,1'
input_str = '1,2,9,2,3,1,9'
result = process_input_string(input_str)
print(result)
