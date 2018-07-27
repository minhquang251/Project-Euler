import math
import time
def findFibNum(term):
    fib_num = [1,1]
    for i in range(3, term+1):
        fib_num.append(fib_num[i-3]+fib_num[i-2])
    return fib_num[term-1]

def findTotalNum(n):
    return int(math.log10(n))+1

start= time.time()
n=1
while findTotalNum(findFibNum(n)) <= 1000:
    if findTotalNum(findFibNum(n)) == 1000:
        print(n)
        break
    n += 1
elapsed = time.time() - start
print("Result found in %f seconds"%elapsed)