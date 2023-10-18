'''
If you put m identical apples on n identical plates, and allow some of the plates to be empty, how many different ways are there?
Note: If there are 7 apples and 3 plates, (5,1,1) and (1,5,1) are considered to be the same division.

Hint:
1. Assuming one plate is empty, the (m,n) problem is translated into placing m apples on n-1 plates, i.e. (m,n-1)
2. Assuming that all plates are loaded with apples, then there is at least one apple on each plate, that is, 
   there are at most m-n apples left, and the problem translates to putting m-n apples on n plates
'''

def f(m,n):
    if m<0 or n<0:
        return 0
    elif m==1 or n==1:
        return 1
    else:
        return f(m,n-1)+f(m-n,n)



# Example usage:
apple = 7
dish = 3
print(f(apple, dish))
