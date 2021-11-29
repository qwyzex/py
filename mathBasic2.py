# (</>)LIBRARY
class color:
    # PRIMARY COLOR
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PINK = '\033[35m'
    LIGHBLUE = '\033[36m'
    GREY = '\033[37m'
    # BACKGROUND COLOR
    BGWHITE = '\033[7m'
    BGBLACK = '\033[40m'
    BGRED = '\033[41m'
    BGGREEN = '\033[42m'
    BGYELLOW = '\033[43m'
    BGBLUE = '\033[44m'
    BGPINK = '\033[45m'
    BGLIGHBLUE = '\033[46m'
    BGGREY = '\033[47m'
    # BORDER
    BORDER = '\033[51m'
    # STYLE
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    IDKWHATITSCALLED = '\033[9m'
    # LIGHTER PRIMARY COLOR (+90)
    # END
    ENDC = '\033[m'


# (?) RULES
rule1 = "1 - ALWAYS INPUT THE ANSWER AS A NUMBER NOT A WORD"
rule2 = "2 - IF YOU ASKED TO INSERT A FORMULA, THE ARITHMETIC SIGN IS:\n" \
        "    TIMES    (x) ==> (*)\n" \
        "    DIVIDE   (÷) ==> (/)\n" \
        "    PLUS     (+)\n" \
        "    MINUS    (-)"
rule3 = "3 - ANY VALUE e.g.(Centimeters, Kilometers, Pounds .etc) SHOULD WRITTEN IN LOWERCASE"

print(color.BLUE + "\n    RULES!\n" + rule1 + "\n\n" + rule2 + "\n\n" + rule3 + "\n" + color.ENDC)
print("PRESS ENTER TO CONTINUE")
input("")

# (#) TEST BEGIN
print("SOLVE THE PROBLEM WITHOUT GOOGLING NOR USING CALCULATOR AND ASK AN EDUCATION FORUM!\n")

# (1) NUMBER ONE
print(color.YELLOW + "1. ((36+(-19)+6)x54.5)+73-(15x4+√9) =")
soal1 = input("")

print("")

# (2) NUMBER TWO
print("2. Zoe has 3 apple, she give one apple to Tom, She eat one for herself,\nand bring back one home. What is the formula for mass of the Sun?")
soal2 = input("")

print("")

# (3) NUMBER THREE
print("3. Simplify this statement perfectly : (x₄ + y₄ + 4x₃y + 4xy₃ 6x₂y₂)!")
soal3 = input("")

print("")

# (4) NUMBER FOUR
print("4. 3 x 4 =")
soal4 = input("")

print("")

# (5) NUMBER FIVE
print("5. Password:" + color.ENDC)
soal5 = input("")

# (%) SCORING
print("\n<=============== TEST RESULT ===============>\n")

finalscore = 0

print("NUMBER 1")
if soal1 == "3334.5":
    print(color.GREEN + "Correct\n" + color.ENDC)
    finalscore += 20
else:
    print(color.RED + "Wrong\n" + color.ENDC)
    finalscore += 0

print("NUMBER 2")
if soal2 == "1989*10^30kg":
    print(color.GREEN + "Correct\n" + color.ENDC)
    finalscore += 20
else:
    print(color.RED + "Wrong\n" + color.ENDC)
    finalscore += 0

print("NUMBER 3")
if soal3 == "(x+y)^4":
    print(color.GREEN + "Correct\n" + color.ENDC)
    finalscore += 20
else:
    print(color.RED + "Wrong\n" + color.ENDC)
    finalscore += 0

print("NUMBER 4")
if soal4 == "12":
    print(color.GREEN + "Correct\n" + color.ENDC)
    finalscore += 20
else:
    print(color.RED + "Wrong\n" + color.ENDC)
    finalscore += 0

print("NUMBER 5")
if soal5 == "qprx0791":
    print(color.GREEN + "Correct\n" + color.ENDC)
    finalscore += 20
else:
    print(color.RED + "Wrong\n" + color.ENDC)
    finalscore += 0

# ($) FINAL SCORE

print("Total Score :")
if finalscore >= 80:
    print(color.GREEN + str(finalscore) + color.ENDC + "/100")
elif finalscore >= 60:
    print(color.YELLOW + str(finalscore) + color.ENDC + "/100")
else:
    print(color.RED + str(finalscore) + color.ENDC + "/100")

# print(str(finalscore) + "/100")
# print(finalscore, "/100")

# (&) FINAL MESSAGE

if finalscore == 100:
    print(color.GREEN + "\nPERFECT! That was amazing! Congratulations!" + color.ENDC)
elif finalscore >= 80:
    print(color.GREEN + "\nCongratulations! You pass the test." + color.ENDC)
elif finalscore >= 60:
    print(color.YELLOW + "\nGood, but not enough..." + color.ENDC)
else:
    print(color.RED + "\nSorry, you didn't pass the test..." + color.ENDC)
