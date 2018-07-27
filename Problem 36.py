import time, math
def int_to_bin(n):
    result = bin(n)
    result = result[2:]
    return int(result)
def isPalindrome(n):
    result = 0
    number = n
    for i in range(int(math.log10(n))+1):
        result = result*10 + number%10
        number = number//10
    if result == n:
        return True
    return False
def problem_36():
    sum = 0
    for i in range(1, 10**6):
        if isPalindrome(int_to_bin(i)) and isPalindrome(i):
            sum += i
    return sum


start = time.time()
print(problem_36())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))