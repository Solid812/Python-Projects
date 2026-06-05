import os

def clear():
    os.system("cls")

def pausi():
    input("Press any key to continue")

def menu():
    epanal = False
    while not epanal:
        print("Ti epithimis?")
        choice1 = input("1.Prosthesi\n2.Afairesi\n3.Pollaplasiasmo\n4.Dieresi\n(5) Exit\n:")

        if choice1 not in ['1', '2', '3', '4', '5']:
            clear()
            print("Apo 1-5")
        else :
            return choice1

def calculate(choice, a, b):
    if choice == "1":
        return f"To apotelesma einai {a + b}"

    elif choice == '2':
        return f"To apotelesma einai {a - b}"

    elif choice == '3':
        return f"To apotelesma einai {a * b}"

    elif choice == '4':
        if b == 0:
            return "Den ginete diairesi me to 0"
        else:
            return f"To apotelesma einai {a / b}"

#main
epanal = False
while not epanal:
    choice1 = menu()
    clear()

    if choice1 == '5':
        break

    epanal2 = False
    while not epanal2:
        try:
            a = int(input("Dose num : ")) 
            b = int(input("Dose num : "))
            epanal2 = True
        except ValueError:
            print("Dexete mono arithmous")

    print(calculate(choice1, a, b))
    pausi()
    clear()