import time, math


def problem_45():
    n = 1
    term = 0
    while True:
        triangle = n*(n+1)/2
        if is_hexagonal(triangle) and is_pentagonal(triangle):
            term += 1
            if term == 3:
                return int(triangle)
        n += 1


def is_pentagonal(x):
    if (1+math.sqrt(1+24*x))/6 == int((1+math.sqrt(1+24*x))/6):
        return True
    return False


def is_hexagonal(x):
    if (1+math.sqrt(1+8*x))/4 == int((1+math.sqrt(1+8*x))/4):
        return True
    return False


start = time.time()
print(problem_45())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))