import math
import time
start = time.time()

def isAbundant(n):
    lst = set()
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            if i == 1:
                lst.add(i)
            else:
                lst.add(i)
                lst.add(n/i)
    if sum(lst) > n:
        return True

AbundantList = []
AbundantSum = set()
result = 0
for i in range(2, 28124):
    if isAbundant(i):
        AbundantList.append(i)
for i in AbundantList:
    for j in AbundantList:
        if j+i < 28124:
            AbundantSum.add(j+i)
print(AbundantList)
print(AbundantSum)
for i in range(1, 28124):
    if i not in AbundantSum:
        result += i
print(result)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))
