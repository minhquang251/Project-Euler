import time
import math


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


def Trunc(n):
    m = n
    q = n
    for i in range(int(math.log10(n)+1)):
        sum = ''
        if isPrime(m) and isPrime(q):
            if int(math.log10(m))+1 != 1:
                string = list(str(m))
                string.pop(0)
                for j in string:
                    sum += j
                m = int(sum)
            q = q//10
        else:
            return False
    return True


start = time.time()
lst = []
for i in range(11, 10**6):
    if Trunc(i):
        lst.append(i)
print(sum(lst))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))