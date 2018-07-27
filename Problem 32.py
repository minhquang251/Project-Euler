import itertools, time
def generate_permu(w):
    permu_set = set(itertools.permutations(w))
    permu = []
    for i in permu_set:
        string = ''.join(j for j in i)
        permu.append(string)
    return permu
def find_pandigital_prod(string):
    lst = []
    for i in range(1,4):
        if int(string[0:i])*int(string[i:i+2]) == int(string[i+2:]):
            lst.append(int(string[i+2:]))
        if int(string[0:i])*int(string[i:i+3]) == int(string[i+3:]):
            lst.append(int(string[i+3:]))
        if int(string[0:i])*int(string[i:i+4]) == int(string[i+4:]):
            lst.append(int(string[i+4:]))
    return lst
def problem_32():
    lst = generate_permu('123456789')
    result = []
    for i in range(len(lst)):
        pan_lst = find_pandigital_prod(lst[i])
        if len(pan_lst) > 0:
            for j in pan_lst:
                result.append(j)
    return sum(set(result))


start = time.time()
print(problem_32())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))