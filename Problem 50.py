import math
import time
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def problem_50():
    prime = [2]
    for i in range(3,10**5):
        if isPrime(i):
            prime.append(i)
    total = 0
    standard_diff = 0
    for i in prime:
        total += i
        if isPrime(total) and total < 10**6:
            standard_diff = prime.index(i)
    for i in range(1,10**6):
        if sum(prime[i:standard_diff+i]) > 10**6:
            break
        for j in range(i,-1, -1):
            if isPrime(sum(prime[j:standard_diff+i])) and sum(prime[j:standard_diff+i]) < 10**6:
                if standard_diff+i-j > standard_diff:
                    total = sum(prime[j:standard_diff+i])
                    standard_diff += i-j
    return total


start = time.time()
print(problem_50())
elapsed = time.time() - start
print("Result found in %f seconds" %(elapsed))
