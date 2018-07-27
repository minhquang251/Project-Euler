import math,time
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
def problem_7(n):
    result = []
    num = 2
    while len(result) < n:
        if isPrime(num):
            result.append(num)
        num += 1
    return result[-1]
start = time.time()
print(problem_7(10001))
elapsed = time.time() - start
print("Result found in %f seconds" % elapsed)
