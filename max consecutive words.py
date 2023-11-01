'''
The character string S consists of lowercase letters and is of length n. Define an operation that can pick any two adjacent letters in a string to swap each time. 
Ask what is the maximum number of consecutive positions in a string that have the same letter after at most m swaps?
'''

def max_consecutive_positions_with_swaps(s, m):
    
    res = 1

    for c in range(ord('a'), ord('z') + 1):
        c = chr(c)
        pos = []
        for i in range(len(s)):
            if c == s[i]:
                pos.append(i)  # searches for all positions in the input string where that letter appears and stores these positions in the pos list.
        if len(pos) < 2:
            continue

        ans = 1
        dp = [[0 for _ in range(len(pos))] for _ in range(len(pos))]   # dynamic programming
        for length in range(2, len(pos) + 1):   # DP process calculates the maximum consecutive positions for different lengths of contiguous letters
            for i in range(len(pos) - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] + pos[j] - pos[i] + 1 - length
                if dp[i][j] <= m:
                    ans = length

        res = max(res, ans)

    return res

# Example usage:
# s = "abbaaac"
s = 'abcbaa'
m = 2

result = max_consecutive_positions_with_swaps(s, m)
print(result)
