def append_zero_at_end(l):
    zero = 0
    non_zero = []
    for i in range(len(l)):
        if i == 0:
            zero += 1
        else:
            non_zero.append(i)

    non_zero.extend([0] * zero)
    return non_zero


print(append_zero_at_end([1,2,0,4,0,5,0,6]))