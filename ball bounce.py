'''
Suppose a ball falls freely from any height and bounces back to half of its original height after each landing; Fall again, 
ask: in the fifth landing, a total of how many meters? How high is the 5th rally?
'''

def ball_fall_and_bounce(initial_height):
    total_distance = initial_height

    for i in range(4):
        initial_height /= 2
        total_distance += 2 * initial_height  # Add both the fall and the bounce height

    initial_height /= 2
    
    return total_distance, initial_height

# Example usage
initial_height = 1
total_distance, fifth_bounce_height = ball_fall_and_bounce(initial_height)

print(total_distance)
print(fifth_bounce_height)

