import time
start = time.time()
f = open("Problem 22.txt")
lst = sorted(f.read().replace('"','').split(','))
alphabet_dict = {}
for i in range(65,91):
    alphabet_dict.update({chr(i): (i-64)})
total = 0
for name in lst:
    score_1 = 0
    for char in name:
        score_1 += alphabet_dict[char]
    total += (score_1*(lst.index(name)+1))
print(total)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))