import time
amicable_set = set()
def sum_div(n):
    sum = 0
    for i in range(1, n//2 + 1):
        if n%i == 0:
            sum += i
    return sum


start = time.time()
lst = [-1]
for n in range(1,10000):
    lst.append(sum_div(n))

for n in range(1,10000):
    if lst[n] < 10000:
        if lst[lst[n]] == n and lst[n] != n:
            amicable_set.add(n)
sorted(amicable_set)
print(sum(amicable_set))
elapsed = time.time() - start
print("Result found in %f seconds" %(elapsed))