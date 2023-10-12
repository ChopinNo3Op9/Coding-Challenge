'''
Find all the possible plans for buying A: 5, B: 3, and C: 1/3 when the total money is 100 and the total number of A, B, and C to buy is 100
x + y + z = 100
5x + 3y + z/3 = 100
'''

for x in range(21): # all possible x
    y = (100 - 7*x)/4 # from the above equation system
    z = 100 - x -y
    if y == int(y) and y >= 0 and z >= 0:
        print(x, int(y), int(z))