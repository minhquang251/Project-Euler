import time
def print_board(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if j == len(array)-1:
                print(array[j][i])
                break
            else:
                print(array[j][i], end="\t")


def findSumDiagonal(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][i] + array[len(array)-1-i][i]
    return sum-1

start = time.time()
length = int(input("Enter an odd length:"))
lst = [[0 for i in range(length)]for j in range(length)]
lst[length//2][length//2] = 1
const = 3
for i in range(1, length//2 +1):
    lst[length//2+i][length//2 -i] = const**2
    x_place = length//2 + i
    y_place = length//2 -i
    value = const**2
    for j in range(1, const):
        lst[x_place - j][y_place] = value - j
        if j == const - 1:
            x_place -= j
            value -= j
    for j in range(1, const):
        lst[x_place][y_place+j]= value-j
        if j == const -1:
            y_place += j
            value -= j
    for j in range(1, const):
        lst[x_place+j][y_place] = value - j
        if j == const - 1:
            x_place += j
            value -= j
    for j in range(1, const -1):
        lst[x_place][y_place-j] = value - j

    const += 2

print_board(lst)
elapsed = time.time() - start
print("Result is %d"%(findSumDiagonal(lst)))
print("Result found in %f seconds"%(elapsed))


