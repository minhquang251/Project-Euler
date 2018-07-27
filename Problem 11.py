import time
start = time.time()
f = open("Problem 11.txt","r")
lst = f.read()
print(lst)
lst = lst.split("\n")
print(lst)
L = [i.split() for i in lst]
print(L)
L = [[int(i) for i in j] for j in L]
print(L)

max_prod = 0

#Horizontally
for i in range(0, 20):
   for j in range(0, 17):
        prod = L[j][i]*L[j+1][i]*L[j+2][i]*L[j+3][i]
        if prod > max_prod:
            max_prod = prod

#Vertically
for i in range(0, 20):
    for j in range(0, 17):
        prod = L[i][j]*L[i][j+1]*L[i][j+2]*L[i][j+3]
        if prod > max_prod:
           max_prod = prod

#Diagonally
for i in range(0, 17):
    for j in range(0, 17):
        prod = L[i][j]*L[i+1][j+1]*L[i+2][j+2]*L[i+3][j+3]
        if prod > max_prod:
            max_prod = prod

for i in range(0, 17):
    for j in range(3, 20):
        prod = L[i][j]*L[i+1][j-1]*L[i+2][j-2]*L[i+3][j-3]
        if prod > max_prod:
            max_prod = prod

print(max_prod)
f.close()
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))