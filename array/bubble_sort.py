def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                l[j], l [j+1] =l[j+1], l[j] 
    return l    


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))