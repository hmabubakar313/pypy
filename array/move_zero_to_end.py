def move_zero_to_end(l1):
    non_zero_l = []
    for x in l1:
        if x != 0:
            non_zero_l.append(x)
    zero_count = len(l1) - len(non_zero_l)
    result = non_zero_l + [0] * zero_count

    return result


print(move_zero_to_end([0,1,0,0,12,2,0]))
