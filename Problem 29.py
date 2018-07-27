import time
start = time.time()
lst = set()
for a in range(2, 101):
    for b in range(2, 101):
        lst.add(a**b)
print("Result is %d"%(len(lst)))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))