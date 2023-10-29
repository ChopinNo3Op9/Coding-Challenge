'''
Output the number of 7-related digits between 1 and n.
A number related to 7 is a number that is a multiple of 7, or a number that contains 7 (e.g., 17, 27, 37...). 70, 71, 72, 73...)
'''

def contain_7 (n):
    nlist = [int(s) for s in str(n)]
    if 7 in nlist:
        return True
    return False

def select_7(r):
    count = 0

    for i in range(1, r+1):
        if contain_7(i):
            count += 1
        elif i % 7 == 0:
            count += 1
    return count

# test
ran = 20
# ran = 10
print(select_7(ran))

