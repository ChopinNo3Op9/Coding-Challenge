'''
Given the information (name, grades) sequence of some students, arrange their information according to grades from high to low or from low to high. 
An example: 
jack 70 
peter 96 
Tom 70 
from high to low:
peter 96 
jack 70 
Tom 70 
From low to high:
jack 70 
Tom 70 
peter 96
'''


def reorder(li):

    order = li[0]
    subli = li[1:]
    data = [(s.split()[0], s.split()[1]) for s in subli]

    sorted_data = sorted(data, key=lambda x: x[1], reverse=(order == '0'))
    for name, number in sorted_data:
        print(f"{name} {number}")


# test
inputstring = ['0', 'fang 90', 'yang 50', 'ning 70']
# inputstring = ['1', 'fang 90', 'yang 50', 'ning 70']
reorder(inputstring)