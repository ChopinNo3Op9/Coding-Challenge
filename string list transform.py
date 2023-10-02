'''
Some basic transformation between list and string is shown.
'''

def listlist2stringlist(s):
    stringlist = [' '.join(map(str, element)) for element in s]
    return stringlist

def stringlist2listlist(s):
    listlist = [[int(x) for x in element.split()] for element in s]
    return listlist


def listlist2multilines(s):
    linelist = [' '.join(map(str, element)) for element in s]
    return '\n'.join(linelist)

def stringlist2multilines(s):
    return '\n'.join(s)




# test
a = [[10, 2, 5],[7, 1, 0],[9, 9, 9],[1, 23, 12],[6, 5, 9]]
print(listlist2stringlist(a))
print("================================================")
b = ['10 2 5', '7 1 0', '9 9 9', '1 23 12', '6 5 9']
print(stringlist2listlist(b))
print("================================================")
c = [[10, 2, 5],[7, 1, 0],[9, 9, 9],[1, 23, 12],[6, 5, 9]]
print(listlist2multilines(c))
print("================================================")
d = ['10 2 5', '7 1 0', '9 9 9', '1 23 12', '6 5 9']
print(stringlist2multilines(d))