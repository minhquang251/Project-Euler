import time
from datetime import date
start = time.time()
number_of_sunday = 0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year, month, 1).isoweekday() == 7:
            number_of_sunday += 1
print(number_of_sunday)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))