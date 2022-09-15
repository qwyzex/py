import math

def abc(a, b, c):
    p = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    n = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)

    x = [p, n]

    return x

def perfect(a, b, c):
    x = None
    r = 0
    s = math.pow(-b / 2, 2)

    if a == 1:
        r += -c
        r += s
        r = math.sqrt(r)
        x = [r + -b / 2, -r + -b / 2]
    else:
        print("Not yet to support x^2 coefficient other than 1")

    return x

print(abc(1, -6, 5))
print(perfect(1, -6, 5))
