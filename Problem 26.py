#Check http://mathworld.wolfram.com/FullReptendPrime.html for more useful information about full reptend prime
#Check Problem 26.jpg for how to prove it
import math, time


def problem_26():
    print(generate_full_reptend_prime(1000)[-1])
    return


def isPrime(n):
    if n == 1 or n <= 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


def generate_prime(n):
    result =[]
    for i in range(n):
        if isPrime(i):
            result.append(i)
    return result


def generate_full_reptend_prime(n):
    prime_lst = generate_prime(n)
    result = []
    for i in prime_lst:
        if 10**(i-1) % i == 1:
            is_full_rep = True
            for j in range(i-2,0,-1):
                if 10**j % i == 1:
                    is_full_rep = False
                    break
            if is_full_rep == True:
                result.append(i)
    return result


start = time.time()
problem_26()
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))