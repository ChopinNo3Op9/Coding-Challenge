'''
Calculates the cube root of a floating point number.
'''

def cube_root(string):
    number = float(string)
    if number < 0:
        return -((-number)**(1/3))
    else:
        return number**(1/3)

# test
# a = '2.7'
a = '-5'
print(f"{cube_root(a):.1f}")
