import time, sys


def problem_31_brute_force(target):
    count = 0
    for h in range(target//200 +1):
        for g in range(target//100 +1):
            for f in range(target//50 +1):
                for e in range(target//20 +1):
                    for d in range(target//10 +1):
                        for c in range(target//5 +1):
                            for b in range(target//2 +1):
                                a = target - 200*h - 100*g - 50*f - 20*e - 10*d - 5*c - 2*b
                                if a >= 0 and type(a) == int:
                                    count += 1
    return count


def problem_31_dynamic_programming(money, coin_index):#Project Euler's Reference
    count = 0
    if coin_index <= 0:
        return 1
    m = money
    if memoiz_list[m][coin_index] > 0:
        return memoiz_list[m][coin_index]
    while money >= 0:
        count += problem_31_dynamic_programming(money, coin_index - 1)
        money -= coin_list[coin_index]
    memoiz_list[m][coin_index] = count
    return count


def problem_31(money, coin_index): #My solution (cannot solve big number such as 10000)
    if coin_index < 0:
        return 0
    if coin_index == 0 or money == 0:
        return 1
    if memoiz_list[money][coin_index] > 0:
        return memoiz_list[money][coin_index]
    if coin_list[coin_index] > money:
        return problem_31(money, coin_index - 1)
    memoiz_list[money][coin_index] = problem_31(money, coin_index-1)+ \
                                     problem_31(money-coin_list[coin_index],coin_index)
    return memoiz_list[money][coin_index]

def problem_31_brilliant_solution(money):
    nb_ways = [1] + [0] * money
    for c in coin_list:
        for v in range(money + 1 - c):
            nb_ways[v + c] += nb_ways[v]
    return nb_ways[-1]

start = time.time()
coin_list = [1,2,5,10,20,50,100,200]
memoiz_list = [[0,0,0,0,0,0,0,0] for i in range(201)]
print(problem_31(200,7)) #Replace problem_31_dynamic_programming() with problem_31
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))