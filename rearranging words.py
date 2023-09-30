from itertools import permutations

# word = "cbaa"
word = "baca"

permuted_words = [''.join(p) for p in permutations(word)]

unique_permutations = sorted(set(permuted_words))

print(unique_permutations)

if unique_permutations[-1] == word:
    print("no answer")
else:
    print(unique_permutations[unique_permutations.index(word) + 1])

