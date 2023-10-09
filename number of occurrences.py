'''
Outputs the number of occurrences of that character in the input string.
'''

def occurrences(s):
    find = s[0][0].lower()
    target = s[1][0].lower()
    d = {}
    d[target] = 0
    for s in find:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

    return d[target]

# test
# string = [['ABCabc'], ['A']]
string = [['8 8 8  8A i i OOI              IIIaa'], ['A']]
print(occurrences(string))

