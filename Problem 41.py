import math,time, itertools
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def gen_n_digit_pandigit_prime(n):
    result = []
    arr = ''
    for i in range(1,n+1):
        arr += str(i)
    lst = list(itertools.permutations(arr, n))
    for i in range(len(lst)):
        num = ''
        for j in range(n):
            num += lst[i][j]
        if isPrime(int(num)):
            result.append(int(num))
    result.sort()
    if len(result) == 0:
        return None
    return result[-1]

def problem_41():
    result = []
    for i in range(4, 9):
        added = gen_n_digit_pandigit_prime(i)
        if added != None:
            result.append(added)
    return result[-1]

start = time.time()
print(problem_41())
elapsed = time.time() - start
print('Result found in %f seconds'%(elapsed))