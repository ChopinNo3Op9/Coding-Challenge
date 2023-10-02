'''
Sort the data based on the kth column.
'''



def reorder(s, k):
    split_data = [(line, int(line.split()[k-1])) for line in s]
    sorted_data = sorted(split_data, key=lambda x: x[1])
    sorted_lines = [line[0] for line in sorted_data]

    return '\n'.join(sorted_lines)



# test
data = ["10 2 5", "7 1 0", "9 9 9", "1 23 12", "6 5 9"]
k = 3
print(reorder(data, k))