def duplicates(l):
    counter = {}
    duplicates = []
    
    for item in l:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    for item, count in counter.items():
        if count > 1:
            duplicates.append(item)
    
    return duplicates



print(duplicates([1,2,3,4,5,1]))