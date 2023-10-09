'''
Find the least common multiple (LCM) of two positive integers A and B.
'''

def gcd(a, b):
    while b:  # b = 0 end
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


# test
# print(lcm(4, 7))
print(lcm(14, 35))