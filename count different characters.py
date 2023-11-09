'''
Input a positive integer, in order from smallest to largest output all its prime factors (repeat also want to list) (such as 180 prime factors 2, 2, 3, 3, 5)
'''

def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(str(divisor))
            n = n // divisor
        else:
            divisor += 1

    return ' '.join(factors)

# test
num = 180
print(prime_factors(num))
