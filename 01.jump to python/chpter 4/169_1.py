def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)

for n in range(1,10):
    print(fib(n))

