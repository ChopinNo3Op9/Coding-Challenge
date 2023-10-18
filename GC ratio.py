'''
A DNA sequence consists of a permutation of four letters A/C/G/T. 
The ratio of G to C (defined as the GC-Ratio) is the total number of occurrences of the letters G and C in the sequence divided by the total number of letters (that is, the sequence length). 

Given a very long DNA sequence, and a bounded substrings length N, 
help the researcher find the first substrings of length N with the highest GC-Ratio from left to right in the given DNA sequence.

The substrings of DNA sequence ACGT are: ACG, CG, CGT, etc., but not AGT, CT, etc
'''


def find_highest_gc_ratio_substring(dna_sequence, N):
    if len(dna_sequence) < N:
        return "DNA sequence is too short for the specified substring length."

    max_gc_ratio = 0
    max_gc_substring = ""

    for i in range(len(dna_sequence) - N + 1):
        substring = dna_sequence[i:i + N]
        gc_count = substring.count('G') + substring.count('C')
        gc_ratio = gc_count / N

        if gc_ratio > max_gc_ratio:
            max_gc_ratio = gc_ratio
            max_gc_substring = substring

    return max_gc_substring

# Example usage:
# dna_sequence = 'ACGT'
# N = 2
dna_sequence = 'AACTGTGCACGACCTGA'
N = 5
print(find_highest_gc_ratio_substring(dna_sequence, N))
