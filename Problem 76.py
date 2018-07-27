import time


summand_list = [i for i in range(1,100)]
memoiz_list = [[0 for j in range(len(summand_list))] for i in range(len(summand_list)+2)]


def problem_76(total, summand_index): #My solution (cannot solve big number such as 10000 :( )
    if summand_index < 0:
        return 0
    if summand_index == 0 or total == 0:
        return 1
    if memoiz_list[total][summand_index] > 0:
        return memoiz_list[total][summand_index]
    if summand_list[summand_index] > total:
        return problem_76(total, summand_index - 1)
    memoiz_list[total][summand_index] = problem_76(total, summand_index-1)+ \
                                        problem_76(total-summand_list[summand_index],summand_index)
    return memoiz_list[total][summand_index]


start = time.time()
print(problem_76(100,98))
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))