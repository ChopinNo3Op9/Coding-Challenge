'''
Return FizzBuzz if a number is multiple of 3 and 5, return Buzz if multiple of 5, return Fizz if multiple of 3, return i otherwise.
'''

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


# test
n = 15
fizzbuzz(n)
