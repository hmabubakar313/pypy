def intersection(l1, l2):
    print("l1 ,l2:",l1, l2)
    intersection = [x for x in l1 if x in l2]
    print("intersection", intersection)
    return intersection


print(intersection([4,5,6], [1,4,2, 3]))