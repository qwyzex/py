# WITH {FOR} LOOP

for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'\

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"
print(variable15)

# WITH DICTIONARY

var = "a"
val = 9
dict1 = {var: val}
print(dict1["a"])

