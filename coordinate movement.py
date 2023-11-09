'''
Develop A coordinate calculation tool where A means move left, D means move right, W means move up, and S means move down. Move from the point (0,0), read some coordinates from the input string, and output the final input result to the output file.
Input:
The legal coordinates are A(or D or W or S) + numbers (within two digits)
Between the coordinates; Separate.
Invalid coordinates need to be discarded. Such as AA10; A1A; $% $; YAD; Let's wait.
Here is a simple example:
A10; S20; W10; D30; X; A1A; B10A11;; A10;
Processing process:
Starting point (0,0)
+ A10 = (-10,0)
+ S20 = (-10,-20)
+ W10 = (-10,-10)
+ D30 = (20,-10)
+ x = invalid
+ A1A = invalid
+ B10A11 = invalid
+ One empty does not affect
+ A10 = (10,-10)
Result (10, -10)
'''

def process_coordinates(input_str):
    x, y = 0, 0

    coordinates = input_str.split(';')
    # print(coordinates)

    for coord in coordinates:
        coord = coord.strip()  # Remove leading and trailing spaces
        if coord:
            # Check if the coordinate is valid
            if coord[0] in ('A', 'D', 'W', 'S') and coord[1:].isdigit():
                distance = int(coord[1:])
                
                if coord[0] == 'A':
                    x -= distance
                elif coord[0] == 'D':
                    x += distance
                elif coord[0] == 'W':
                    y += distance
                elif coord[0] == 'S':
                    y -= distance
            else:
                continue

    print(f"{x},{y}")

# Example usage
# input_string = "A10; S20; W10; D30; X; A1A; B10A11;; A10;"
input_string = 'ABC;AKL;DA1;'
process_coordinates(input_string)
