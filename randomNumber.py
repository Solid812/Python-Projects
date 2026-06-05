import random

def tixaiosArithmos():
    secretNum = random.randint(1,100)
    prospatheies = 0
    
    print("Μάντεψε τον κρυφό αριθμό (1-100)")

    guess = False
    while not guess:
        try:
            num = int(input("Μάντεψε : "))
            prospatheies += 1

            if num < secretNum:
                print("Ο αριθμος είναι μεγαλύτερος")
            elif num > secretNum:
                print("Ο αριθμος είναι μικρότερος")
            else :
                print(f"Μπράβο τον βρήκες σε {prospatheies} προσπάθειες")
                guess = True

        except ValueError:
            print("Λάθος τιμή, δέχεται μόνο αριθμούς")

            
# Main 
tixaiosArithmos()