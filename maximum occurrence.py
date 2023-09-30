'''
Give a string, return the first character which has the maximum occurrence.
'''

def max_occurrence_first(string):

    letter_count = {}

    for s in string:
        if s in letter_count:
            letter_count[s] += 1
        else:
            letter_count[s] = 1

    max_letter = None
    max_count = 0
    for letter, count in letter_count.items():
        if count > max_count:
            max_letter = letter
            max_count = count

    return max_letter, max_count
    
# test
input_string = "heeeelllloo"
result_char, result_count = max_occurrence_first(input_string)
print(result_char)
