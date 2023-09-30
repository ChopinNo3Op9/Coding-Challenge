'''
Wendy and Bob are playing games. Wendy moves first and should remove a w with both adjacent w on both sides. Then Bob moves b, unitil someone cannot remove anymore.
'''

def game_winner(s):
    turn = "Wendy"
    
    while True:
        found = False 
        
        if 'www' in s and turn == "Wendy":
            s = s.replace('www', 'ww', 1) 
            found = True
        elif 'bbb' in s and turn == "Bob":
            s = s.replace('bbb', 'bb', 1)
            found = True
        
        turn = "Bob" if turn == "Wendy" else "Wendy"

        if not found:
            return turn

# test
# initial_string = "wwwbbbbwww"
# initial_string = "wwbbbbww"
initial_string = "wwwbbbww"
print(game_winner(initial_string))
