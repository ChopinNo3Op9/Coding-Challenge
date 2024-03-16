'''
Three kinds of words legal, all lowercase all uppercase, the first uppercase other lowercase, ask a word at least how many operations can modify the word legal.
It takes a word as input and returns the minimum number of operations needed to make it legal:
'''

def min_operations_to_legal(word):
    # Convert all characters to lowercase
    lower_case = word.lower()
    # Convert all characters to uppercase
    upper_case = word.upper()
    # Capitalize the first character and convert others to lowercase
    capitalize_case = word.capitalize()

    # Calculate the minimum number of operations needed
    min_operations = min(
        len([c1 for c1, c2 in zip(word, lower_case) if c1 != c2]),  # Number of operations to convert to all lowercase
        len([c1 for c1, c2 in zip(word, upper_case) if c1 != c2]),  # Number of operations to convert to all uppercase
        len([c1 for c1, c2 in zip(word, capitalize_case) if c1 != c2])  # Number of operations to convert to capitalized case
    )
    
    return min_operations

# Example usage
word = "ExAmPle"
print("Minimum operations required:", min_operations_to_legal(word))
