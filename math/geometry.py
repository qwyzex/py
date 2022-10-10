f = input("Expression as x : ")

def cordinate(formula):
    x = [-3, -2, -1, 0, 1, 2, 3]
    xy = []

    for n in x:
        xy.append([x[n + 3], formula(n)])

    print(xy)

cordinate(lambda x:eval(f))
