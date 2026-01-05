def fib(n,mem0={}):
    if n in mem0:
        return mem0[n]
    if n <= 1:
        return n
    mem0[n] = fib(n-1,mem0) + fib(n-2,mem0)
    return mem0[n]
print(fib(10))  