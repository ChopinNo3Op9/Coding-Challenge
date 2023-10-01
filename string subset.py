'''
Check if two lists of numbers are subset of the first.
'''

def is_subset(a, b):
    i = 0
    while i < len(b):
        if set(b[i]).issubset(set(a)) == False:
            return False
        i += 1
    return True


# test
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78]
# l = [[1, 2, 3, 4, 5], [10, 11, 12]]
l = [[1, 2, 3, 4, 5], [100, 11, 12]]
print(is_subset(list1, l))