import time

j = 0
start = time.time()

Goal = 999999
factorials = []
v = 1
i = 1
while i < 11:
    factorials.append(v)
    v *= i
    i += 1
v = 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 0
while v >= 0:
    value = Goal // factorials[v]
    Goal -= value * factorials[v]
    v -= 1
    result = result * 10 + numbers[value]
    numbers.pop(value)

elapsed = time.time() - start
print(result)
print("Result found in %f seconds"%(elapsed))