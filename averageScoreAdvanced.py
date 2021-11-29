# SCHOOL "X"

school1 = "smpX"

name11 = "Ihsan"
name11sch = school1
math11 = 96
indsc11 = 82
blamp11 = 62
ave11 = (math11 + indsc11 + blamp11)/3

name12 = "Billy"
name12sch = school1
math12 = 86
indsc12 = 81
blamp12 = 68
ave12 = (math12 + indsc12 + blamp12)/3

print("Average Score of both candidates from X is...")
print("Ihsan :", round(ave11))
print("Billy :", round(ave12))

print("")  # SCHOOL "Y"

school2 = "smpy"

name21 = "Adi"
name21sch = school2
math21 = 88
indsc21 = 69
blamp21 = 49
ave21 = (math21 + indsc21 + blamp21)/3

name22 = "Tina"
name22sch = school2
math22 = 90
indsc22 = 67
blamp22 = 86
ave22 = (math22 + indsc22 + blamp22)/3

print("Average Score of both candidates from Y is...")
print("Adi :", round(ave21))
print("Tina :", round(ave22))

print("")  # AVERAGE SCORE OF EACH SCHOOL

schX = (ave11 + ave12)/2
schY = (ave21 + ave22)/2

print("School X Score is : ", round(schX))
print("School Y Score is : ", round(schY))

print("")  # AVERAGE SCORE OF BOTH SCHOOL

aveSch = (schX + schY)/2

print("Average Score of both school sum is : ", aveSch)

print()  # STATUS
if aveSch >= 76:
    print("Congratulations! Your city pass the test and will soon go to Japan!\nThank you for participate in Global Science Olympiad!")
else:
    print("Sorry, your city's education need to improve in order to join this event.\nThank you for participate in Global Science Olympiad!")

