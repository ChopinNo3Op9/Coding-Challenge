'''
Count the number of 1 in binary format of int.
'''

# def count_ones_in_binary(integer):
#     if integer < 0:
#         return "Please enter a positive integer."
    
#     binary = bin(integer)
#     ones_count = binary.count('1')
    
#     return ones_count

def count_ones_in_binary(integer):
    count = 1
    while integer != 1:
        if integer % 2 == 1:
            count += 1
        integer = integer // 2  # 5//2 = 2
    return count


# Example
positive_integer = 5
# positive_integer = 0
ones_count = count_ones_in_binary(positive_integer)
print(ones_count)
