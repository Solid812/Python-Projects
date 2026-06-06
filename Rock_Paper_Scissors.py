import random
import os

def clear():
    print("\033[H\033[2J", end="")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def game():
    print("***** Πετα/Ψαλιδι/Χαρτι *****")

    name = input("Ονομα παικτη : ")
    npc = input("Ονομα εχθρου : ")

    clear()

    print("***** GAME START *****")
    print("Το παιχνιδι τελιωνει οταν ενας φτασει τους 5 ποντους\n")

    player1 = 0
    ai = 0
    while player1 <= 5 or ai <= 5:

        if player1 == 5 or ai == 5:

            if player1 > ai:
                print(f"Ο {name} νικησε το παιχνιδι")
                return
            else :
                print(f"Ο {npc} νικησε το παιχνιδι")
                return

        if player1 > 0 or ai > 0:
            print(f"{name} : {player1} \n{npc} : {ai}\n")

        while True:
            try:   
                print("(1) Πετρα (2) Ψαλιδι (3) Χαρτι")
                choice = int(input(f"{name} : "))

                if choice not in [1, 2, 3]:
                    print("1, 2 ή 3\n")
                else :
                    break
            except ValueError:
                print("Μονο αριθμους")
        
        choiceAI = random.randint(1, 3)
        print(f"\nΟ {npc} διαλεξε {choiceAI}\n")

        if choice == choiceAI:
            print("Ισοπαλια")

        elif choice == 1 and choiceAI == 2:
            print(f"O {name} νικησε")
            player1 += 1

        elif choice == 1 and choiceAI == 3:
            print(f"O {npc} νικησε")
            ai += 1

        elif choice == 2 and choiceAI == 1:
            print(f"O {npc} νικησε")
            player1 += 1
            
        elif choice == 2 and choiceAI == 3:
            print(f"O {name} νικησε")
            ai += 1
        
        elif choice == 3 and choiceAI == 1:
            print(f"O {name} νικησε")
            player1 += 1

        elif choice == 3 and choiceAI == 2:
            print(f"O {npc} νικησε")
            ai += 1

#main
while True:
    game()  
    choice = input("Thes epileon game? \n(Any) NAI (0) OXI \n: ")     
    if choice == '0':
        break
    