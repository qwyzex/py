import inquirer

question = [
    inquirer.List('choice',
            message="What Function?",
            choices=["LCM", "HCF"]
        )
]

answer = inquirer.prompt(question)
numOne = int(input("First Number  : "))
numTwo = int(input("Second Number : "))

def lcm(one, two):
    _min = None

    if one > two:
        _min = one
    elif one < two:
        _min = two

    found = False

    while found == False:
        if ((_min % one == 0) and (_min % two == 0)):
            found = True
            return _min
        else:
            _min += 1

def hcf(one, two):
    highest = None

    for x in range(1, one and two, 1):
        if ((one % x == 0) and (two % x == 0)):
            highest = x

    return highest

if answer == {'choice': 'LCM'}:
    print(lcm(numOne, numTwo))
elif answer == {'choice': 'HCF'}:
    print(hcf(numOne, numTwo))

