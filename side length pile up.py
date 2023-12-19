'''
Given a list of cubes, when stacking cubes, only pick up either the leftmost or the rightmost cube each time such that the bottom cube is >= the upper cube. 
'''

def pileup(b):
    current = max(b[0], b[-1])
    while b[0] <= current or b[-1] <= current:
        if b[0] > current:
            current = b[-1]
            b.pop(-1)
        elif b[-1] > current:
            current = b[0]
            b.pop(0)
        elif b[0] <= b[-1]:
            current = b[-1]
            b.pop(-1)
        else: 
            current = b[0]
            b.pop(0)


        if len(b) == 0:
            return "Yes"
    return "No"



# test
# blocks = [1, 2, 3, 4, 5, 6, 7]
# blocks = [1, 2, 3, 4, 5, 6, 1]
# blocks = [1, 2, 3, 4, 3]
blocks = [2, 1, 1, 10, 1, 2, 2]
print(pileup(blocks))