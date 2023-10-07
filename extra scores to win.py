'''
Calculate how many more points the first person, a, should win in order to satisfy the condition that they have a score higher or equal to 11 
and higher than the second person, b, by at least 2 points. 
(find the min. If they always same scors, then infinity)
'''

def points_to_win(a, b):
    if a >= 11 and a >= b + 2:
        return 0 
    elif a < 11 and b < 11:
        return 11 - a  # First person needs to reach 11 points first.
    else:
        return max(11 - a, 2 - (a - b))

# test
# a_score = 8
# b_score = 6
# a_score = 30
# b_score = 31
# a_score = 8
# b_score = 8
a_score = 18
b_score = 18
additional_points = points_to_win(a_score, b_score)
print(f"Person a should win {additional_points} more points.")


