import math, time
def isPrime(n):
    if n == 1 or n <= 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
def isQualified(goal, a, b):
    for i in range(2, goal):
        if not isPrime(i*i + i*a +b):
            return False
    return True
def problem_27():
    longest = 0
    for b in range(-1000,1001):
        if isPrime(b): #n = 0 -> S = b
            for a in range(-999,1000):
                if isPrime(1+a+b): # n = 1 -> S = 1 + a + b
                    n = 0
                    count = 0
                    while n >= 0:
                        if not isPrime(n*n + a*n +b):
                            break
                        n += 1
                        count += 1
                    if longest < count:
                        longest = count
                        result = a*b
    return result
start = time.time()
print(problem_27())
elapsed = time.time()-start
print("Result found in %f seconds"%(elapsed))
