def check_anagram(s1,s2):
    if len(s1) == len(s2):
        return True
    else:
        return False

    counter = {}
    counter2 = {}
    for x in s1:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    return counter

    for x in s2:
        if x in counter2:
            counter2[x] += 1
        else:
            counter2[x] = 1
    return counter == counter2

print(check_anagram('listen','silent'))