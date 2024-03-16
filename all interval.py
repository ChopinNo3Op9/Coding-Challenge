'''
Generate all possible intervals without using nested loops is to use a recursive function.
'''

# def generate_intervals(lst, start=0, end=None, intervals=None, generated_intervals=None):
#     if intervals is None:
#         intervals = []
#     if generated_intervals is None:
#         generated_intervals = set()
#     if end is None:
#         end = len(lst)
#     if start < end and (start, end) not in generated_intervals:
#         intervals.append(lst[start:end])
#         generated_intervals.add((start, end))
#         generate_intervals(lst, start, end - 1, intervals, generated_intervals)
#         generate_intervals(lst, start + 1, end, intervals, generated_intervals)
#     return intervals

def generate_intervals(lst):
    intervals = []
    n = len(lst)
    for start in range(n):
        for end in range(start + 1, n + 1):
            intervals.append(lst[start:end])
    return intervals

# Test the function
lst = [1, 2, 3]
intervals = generate_intervals(lst)
print("All intervals:", intervals)
