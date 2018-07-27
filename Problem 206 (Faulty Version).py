import math
def problem_206(lst):
    if full(lst):
        if is_square(to_int(lst)):
            return True
    else:
        first_blank_space = find_blank(lst)
        for i in range(10):
            lst[first_blank_space] = str(i)
            if problem_206(lst):
                return True
            lst[first_blank_space] = ' '
    return False

def full(lst):
    if ' ' not in lst:
        return True
    return False
def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
def to_int(lst):
    result = ''
    for i in range(len(lst)):
        result += lst[i]
    return int(result)
def find_blank(lst):
    if ' ' in lst:
        return lst.index(' ')

#lst = ['1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9','0','0']
lst = ['2',' ','2',' ','9',' ','1']
if problem_206(lst):
    print(lst)