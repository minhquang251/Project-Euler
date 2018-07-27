import time
import math


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def generate_cycle(n):
    array = list(str(n))
    lst = []
    for i in range(len(array)):
        lst.append(added_string(array))
        insert = array.pop()
        array.insert(0, insert)
    for i in lst:
        if not isPrime(i):
            return None
    return lst

def added_string(arr):
    result = ''
    for i in arr:
        result += i
    return int(result)

def problem_35():
    result = set()
    result.add(2)
    for i in range(3,999999):
        if i not in result:
            if '0' not in str(i) and '2' not in str(i) and \
                    '4' not in str(i) and '6' not in str(i) and \
                            '8' not in str(i):
                lst = generate_cycle(i)
                if lst is not None:
                    for j in lst:
                        result.add(j)
    return len(result)


start = time.time()
print(problem_35())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))
