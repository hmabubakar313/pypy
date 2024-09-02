def fib(n):
    if n < 0:
        print("Number is not Correct")
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = fib(9)
print(fib)