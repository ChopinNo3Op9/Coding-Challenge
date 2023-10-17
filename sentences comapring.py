'''
Given two strings s and t, where t is subsequence of s, return the missing part in order.
'''

def missing_part(s, t):
    s_words = s.split(' ')
    t_words = t.split(' ')

    s_index = 0
    t_index = 0
    missing = []

    while s_index < len(s_words) and t_index < len(t_words):
        if s_words[s_index] != t_words[t_index]:
            missing.append(s_words[s_index])
            s_index += 1
        else:
            s_index += 1
            t_index += 1

    missing.extend(s_words[s_index:])

    return missing


# test
s = "I am missing in the sky"
t = "am in the"
# s = "I am missing you in the sky"
# t = "am in the"
print(missing_part(s, t))