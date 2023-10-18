'''
Given a positive integer N representing the number of trains, 0&lt; N&lt; 10, then input the train entry sequence, 
a total of N trains, each train is numbered by the number 1-9, the station has only one direction to enter and exit, 
at the same time in the station of the train, only the last entry station out of the station, the advanced station can exit the station. 

It is required to output the scheme of all train exits, sorted by lexicographical order.
'''


res = []

def dfs(wait, stack, out):
    if not wait and not stack:
        res.append(' '.join(map(str, out)))
    if wait:
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:
        dfs(wait, stack[:-1], out + [stack[-1]])

# Explicit input
n = 3
nums = [1, 2, 3]

dfs(nums, [], [])
for i in sorted(res):
    print(i)
