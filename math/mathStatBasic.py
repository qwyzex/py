from statistics import multimode, median_high, median_low

raw = input("Array : ")

arr = list(map(int, raw.split(' ')))
arr.sort()

# calculate
length = len(arr)
total = 0

# iterate total
for n in arr:
    total += n

even = ''

# define even / odd
if length % 2 == 0:
    even = True
if length % 2 == 1:
    even = False

mean = total / length
median = 0

if len(multimode(arr)) == length:
    modus = "NO MODES"
elif len(multimode(arr)) == 1:
    modus = multimode(arr)[0]
else:
    modus = multimode(arr)

if even:
    median = (arr[int(length / 2 - 1)] + arr[int(length / 2)]) / 2
else:
    median = arr[int((length + 1) / 2 - 1)]

highest = arr[-1]
lowest = arr[0]

print('Mean : ', mean)
print('Median : ', median)
print('Modus : ', modus, '\n')
print('Length : ', length)
print('Total : ', total)
print('Sorted : ', arr, '\n')
print('Highest : ', highest)
print('Lowest : ', lowest)
print('Q1 : ', median_low(arr))
print('Q3 : ', median_high(arr))
