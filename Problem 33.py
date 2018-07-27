import math, time
def is_curious_fr(numer, deno):
    a = numer//10
    b = numer % 10
    c = deno //10
    d = deno % 10
    if numer < deno:
        if a*d == b*c:
            if a == c or b == d:
                return True
        elif 10*a*c + a*d - 10*a*d - b*d == 0:
            if b == c:
                return True
        elif 9*b*c + b*d - 10*a*c == 0:
            if a == d:
                return True
    return False


def problem_33():
    deno = []
    numer = []
    product = 1
    for denominator in range(12,100):
        for numerator in range(11,denominator):
            if denominator % 10 != 0:
                if numerator % 10 != 0:
                    if is_curious_fr(numerator, denominator):
                        numer.append(numerator/math.gcd(int(numerator),int(denominator)))
                        deno.append(denominator/math.gcd(int(numerator),int(denominator)))
    for i in deno:
        product *= i
    for i in numer:
        if math.gcd(int(product), int(i)) != 1:
            product = product/math.gcd(int(product), int(i))
    return product


start = time.time()
print(problem_33())
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))
