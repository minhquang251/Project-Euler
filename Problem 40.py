import time
def loop(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    return arr
def generate_champernowne(n):
    const = ""
    arr = loop(n)
    for i in arr:
        const += str(i)
    return list(const)
def problem_40():
    i = 1
    result = 1
    arr = generate_champernowne(200000)
    while i <= 1000000:
        result *= int(arr[i-1])
        i *= 10
    return result
start = time.time()
print(problem_40())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))