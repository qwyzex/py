# RULES
rule1 = "1 - ALWAYS INPUT THE ANSWER AS A NUMBER NOT A WORD"
rule2 = "2 - IF YOU ASKED TO INSERT A FORMULA, THE ARITHMETIC SIGN IS:\n" \
        "    TIMES    (x) ==> (*)\n" \
        "    DIVIDE   (÷) ==> (/)\n" \
        "    PLUS     (+)\n" \
        "    MINUS    (-)"
rule3 = "3 - ANY VALUE e.g.(Centimeters, Kilometers, Pounds .etc) SHOULD WRITTEN IN LOWERCASE"

print("\n    RULES!\n" + rule1 + "\n\n" + rule2 + "\n\n" + rule3 + "\n")
print("PRESS ENTER TO CONTINUE")
input("")

# NUMBER ONE
print("SOLVE THE PROBLEM WITHOUT GOOGLING NOR USING CALCULATOR AND ASK AN EDUCATION FORUM!\n")
print("1. ((36+(-19)+6)x54.5)+73-(15x4+√9) =")
soal1 = input("")

if soal1 == "3334.5":
    print("Correct, But You're Still Stupid.\n")
else:
    print("Wrong, You Stupid!\n")

# NUMBER TWO
print("2. Zoe has 3 apple, she give one apple to Tom, She eat one for herself,\nand bring back one home. What is the formula for mass of the Sun?")
soal2 = input("")

if soal2 == "1989*10^30kg":
    print("Correct, Anyhow I'm Still Not Sure That You Actually\nCalculate It On Your Own Or Just GOOGLE It.")
else:
    print("Wrong, You're So Stupid!")
