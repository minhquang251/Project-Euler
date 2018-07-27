import math
import time


def root_qualified(p, c):
    if (p+c)**2-2*(p**2) > 0:
        if math.sqrt((p+c)**2-2*(p**2)).is_integer(): #Do some math with Viete Theorem
            return True
        else:
            return False
    else:
        return False


def return_root(p, c, root_array):
    lst = []
    x1 = (p-c-math.sqrt((p+c)**2-2*(p**2)))/2
    x2 = (p-c+math.sqrt((p+c)**2-2*(p**2)))/2
    if x1.is_integer() and x2.is_integer() and x1 > 0 and x2 > 0:
        lst.append(int(x1))
        lst.append(int(x2))
        lst.append(int(c))
        root_array.append(lst)
    return


start = time.time()
max_length = 0
max_root = []
max_perimeter = 0
for perimeter in range(12,1001):
    root_lst = []
    for hypotenuse in range(5, int(perimeter/2) + 1):
        if root_qualified(perimeter, hypotenuse) == True:
            return_root(perimeter, hypotenuse, root_lst)
    if len(root_lst) > max_length:
        max_length = len(root_lst)
        max_root = root_lst[:]
        max_perimeter = perimeter
print(max_root, max_perimeter)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))

