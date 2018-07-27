import time
start = time.time()
f = open("Problem 67.txt") #or Problem 18.txt
lst = f.read()
lst = lst.split("\n")
lst = [i.split() for i in lst]
lst = [[int(i) for i in j] for j in lst]
#Above method will create a multidimensional list like this:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
print(lst)
def findMax(array):
    for row in range(len(array)-2,-1,-1):
        for column in range(row+1):
                array[row][column] += max(array[row+1][column], array[row+1][column+1])
    return array[0][0]

print(findMax(lst))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))
