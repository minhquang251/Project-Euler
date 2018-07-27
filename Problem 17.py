import time
start = time.time()
lst = ["" for i in range(20)]
lst[0] = "zero"
lst[1] = "one"
lst[2] = "two"
lst[3] = "three"
lst[4] = "four"
lst[5] = "five"
lst[6] = "six"
lst[7] = "seven"
lst[8] = "eight"
lst[9] = "nine"
lst[10] = "ten"
lst[11] = "eleven"
lst[12] = "twelve"
lst[13] = "thirteen"
lst[14] = "fourteen"
lst[15] = "fifteen"
lst[16] = "sixteen"
lst[17] = "seventeen"
lst[18] = "eighteen"
lst[19] = "nineteen"
def create_lst(prefix):
    list = [prefix]
    for i in range(1,10):
        x = lst[i]
        word = prefix + x
        list.append(word)
    return list

def append_lst(list, lst):
    for i in list:
        lst.append(i)
    return lst

append_lst(create_lst("twenty"), lst)
append_lst(create_lst("thirty"), lst)
append_lst(create_lst("forty"), lst)
append_lst(create_lst("fifty"), lst)
append_lst(create_lst("sixty"), lst)
append_lst(create_lst("seventy"), lst)
append_lst(create_lst("eighty"), lst)
append_lst(create_lst("ninety"), lst)
def create_list_100(prefix, list):
    list.append(prefix)
    for i in range(1,100):
        list.append(prefix+"and"+list[i])
    return list
create_list_100("onehundred", lst)
create_list_100("twohundred", lst)
create_list_100("threehundred", lst)
create_list_100("fourhundred", lst)
create_list_100("fivehundred", lst)
create_list_100("sixhundred", lst)
create_list_100("sevenhundred", lst)
create_list_100("eighthundred", lst)
create_list_100("ninehundred", lst)
lst.append("onethousand")
total = 0
for i in lst:
    total += len(i)
print(total-4)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))



