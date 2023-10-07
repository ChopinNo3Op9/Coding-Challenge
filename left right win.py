'''
Given a list of 4 numbers [n, x, y, k], n is the total number of quizzes, x is the speed of A, y is the speed of B, k is kth quizzes as the goal.
A is solving quizzes from the left, B is from the right. The one who first reach to k will win.
'''

def quiz_game_outcome(quiz_info):
    n, x, y, k = quiz_info
    time_a = k / x  # Time taken by A to reach quiz k
    time_b = (n - k + 1) / y  # Time taken by B to reach quiz k
    
    if time_a < time_b:
        return "A wins"
    elif time_b < time_a:
        return "B wins"
    else:
        return "Tie"

# Example usage:
# quiz_info = [10, 2, 3, 5]
# quiz_info = [5, 3, 3, 3]
quiz_info = [6, 6, 3, 4]
result = quiz_game_outcome(quiz_info)
print(result)
