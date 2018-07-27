import time
import math
def isQualified(n):
    sum = 0
    m = n
    for i in range(int(math.log10(m))+1):
        sum += math.factorial(n%10)
        n = n//10
    if m == sum:
        return True
    else:
        return False

start = time.time()
lst = []
for i in range(3,9999999):
    if isQualified(i) == True:
        lst.append(i)
print(sum(lst))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))