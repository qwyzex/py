# By default, a module has some hidden variables defined
print({k: v for k, v in globals().items() if not k.startswith("__")})

for i in range(1, 11):
    globals()[f"my_variable_{i}"] = i

print()
print(my_variable_1)
print(my_variable_2)
# and so on

print()
print({k: v for k, v in globals().items() if not k.startswith("__")})

# ====================================================================

for i in range(0, 9):
    globals()[f"my_variable{i}"] = f"Hello from variable number {i}!"


print(my_variable3)
# Hello from variable number 3!

# ====================================================================

for x in range(0, 9):
    globals()['string%s' % x] = 'Hello'
# string0 = 'Hello', string1 = 'Hello' ... string8 = 'Hello'

# ====================================================================
