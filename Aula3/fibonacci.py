import time
from functools import wraps

def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def fibbo(n):
    global adds
    if (n == 0) or (n==1):
        return n
    
    fib1 = fibbo(n-1)
    fib2 = fibbo(n-2)

    adds+=1

    return fib1 + fib2



for i in range(1, 60+1):
    adds = 0
    start_time = time.time()
    print("Fibonacci sequence with " + str(i) + " elements.")
    
    # memoization -> comment to classical fibonacci
    fibbo = memo(fibbo)


    fib = fibbo(i)
    print("Result: " + str(fib))
    print("Add number " + str(adds))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time-start_time)))
    print()
    print()