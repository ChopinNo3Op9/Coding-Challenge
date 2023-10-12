'''
Maximum continuous sequence of 1s in a binary string
'''

def max_continuous_ones(number):
    bi = bin(number)[2:]
    bi_list = bi.split('0')
    maxseq = max(bi_list)

    return len(maxseq)


# test
# ran = 200
ran = 3
print(max_continuous_ones(ran))
