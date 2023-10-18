'''
Each cup of coffee is 5 yuan, and the customer pays 5, 10, and 20 yuan, with no spare change at the beginning.
Input: A sequence of numbers representing the amount a customer pays each time
Output: if you can successfully find change, return true, sequence number;
If it does not succeed, return false, sequence number;
'''

def fun(pays):
    money = {
        5: 0,
        10: 0,
    }
    for i, pay in enumerate(pays):
        if pay == 5:
            money[5] += 1
        elif pay == 10:
            money[5] -= 1
            money[10] += 1
        else:
            money[5] -= 1
            money[10] -= 1

        if min(money.values()) < 0:
            return 'false', i + 1

    return 'true', len(pays)

# p = [5,10,20]
# p = [5,5,10,10,20]
p = [5,5,5,10,10,10]
f, l = fun(p)
print('{},{}'.format(f, l))



