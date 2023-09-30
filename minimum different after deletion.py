'''
Given a list of numers, delete m of them, and return the minimum number of distinct numbers.
'''

def min_diff_elements_after_deletion(arr, m):
    freq_dict = {}

    for element in arr:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    # sort by dict value
    sorted_elements = sorted(freq_dict.items(), key=lambda x: x[1])

    sorted_dict = dict(sorted_elements)
    # print(sorted_dict)

    for key, value in sorted_dict.items():
        if value >= m:
            value -= m
            m = 0
        else:
            m -= value
            value = 0

        sorted_dict[key] = value
    
    # print(sorted_dict)

    return len([element for _, value in sorted_dict.items() if value > 0])

# Example usage:
# arr = [1, 2, 2, 3, 3, 3]
arr = [1, 1, 1, 2, 2, 3, 3, 3]
m = 5
print(min_diff_elements_after_deletion(arr, m))
