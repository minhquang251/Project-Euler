import time
start = time.time()
f = open("Problem 13.txt","r")
lst = f.read()
lst = lst.split("\n")
def sum_list(lst):
    S = 0
    for i in lst:
        S = S + int(i)
    return S
n = sum_list(lst)
while(n>10000000000):
    n = n//10
print(n)
f.close()
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))