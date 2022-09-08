def collatz(starting):
    current = starting
    fin = [starting]

    while 1 not in fin:
        draft = None

        if current % 2 == 0:
            draft = current // 2
        elif current % 2 == 1:
            draft = current * 3 + 1
        else:
            print("INVALID NUMBER")
            break

        fin.append(draft)
        current = draft

    print("\n", fin)

x = int(input("\nPick Starting Number : "))

collatz(x)
