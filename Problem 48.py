import math
import time

def calc_power(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i,i)
    return sum


def find_last_10_digits(n):
    string = str(n)
    return string[-10:]


start = time.time()
print(find_last_10_digits(calc_power(1000)))
elapsed= time.time() - start
print("Result found in %f seconds"%(elapsed))
