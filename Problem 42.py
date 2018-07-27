import time, math
def is_triangle(x):
    if (-1+math.sqrt(1+8*x))/2 == int(-1+math.sqrt(1+8*x))/2:
        return True
    return False
def generate_alphabet_table():
    alphabet_dict = {}
    for i in range(65,91):
        alphabet_dict.update({chr(i): i-64})
    return alphabet_dict
def import_text(text):
    f = open(text)
    lst = f.read().split('"')
    for i in lst:
        if i == "" or i == ",":
            lst.pop(lst.index(i))
    return lst
def problem_42():
    lst = import_text("Problem 42.txt")
    alphabet = generate_alphabet_table()
    count = 0
    for i in lst:
        sum_char = 0
        for j in i:
            sum_char += alphabet[j]
        if is_triangle(sum_char):
            count += 1
    return count
start = time.time()
print(problem_42())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))