import os

def menu():
    print("/***** Menu *****/")
    print("(1) Εισαγωγή Σπουδαστών\n(2) Προβολή Σπουδαστών\n(3) Μέσος όρος")
    choice = input(": ")

    while choice not in ["1","2","3"]:
        choice = ("Λάθος επιλογή\n(1) Εισαγωγή Σπουδαστών\n(2) Προβολή Σπουδαστών\n(3) Μέσος όρος")
    return choice

def eisagogiSpoudaston(onomata , bathmoi):
    choice = "1"
    while choice != "2" :
        print("/***** Εισαγωγή Σπουδαστών *****/")
        onoma = input("Όνομα σπουδαστή : ")
        bathmos = int(input("Βαθμός σπουδαστή : "))
        onomata.append(onoma)
        bathmoi.append(bathmos)
        clear()

        choice = input("Θέλεις να εισάγεις επιπλέον σπουδαστή?\n(1) ΝΑΙ (2) ΟΧΙ\n :")
        clear()
        while choice not in ["1","2"]:
            choice = input("Λάθος επιλογή\nΘέλεις να εισάγεις επιπλέον σπουδαστή?\n(1) ΝΑΙ (2) ΟΧΙ\n :")
            clear()

def emfanisiSpoudaston(onomata , bathmoi):

    if not onomata:
        print("Δεν υπάρχει κάποια καταχώρηση\nΠρώτα εισάγεται τα στοιχεία του/ων σπουδαστή/ές")
    else:
        print("/***** Εμφάνιση Σπουδαστών *****/")

        for i in range(len(onomata)):
            print(f"{i+1}ος Μαθητής\nΌνομα : {onomata[i]} | Βαθμός : {bathmoi[i]}")

        print("/******************************/")    


def mesosOros(bathmoi):
    if not bathmoi:
        print("Δεν υπάρχει κάποια καταχώρηση\nΠρώτα εισάγεται τα στοιχεία του/ων σπουδαστή/ές")

    else:
        sum = 0
        print("/***** Μέσος Όρος Βαθμών *****/")
        for i in range(len(bathmoi)):
            sum = sum + bathmoi[i]
            i=i+1
        print(f"Ο μέσος όρος είναι {sum/i}")
        print("/******************************/")

def clear():
    os.system("cls")

#Main
ListaOnomata = []
ListaBathmoi = []

choice2 = "1"
while choice2 != "2":
    choice = menu()
    clear()

    if choice == "1":
        eisagogiSpoudaston(ListaOnomata , ListaBathmoi)

    if choice == "2":
        emfanisiSpoudaston(ListaOnomata , ListaBathmoi)

    if choice == "3":
        mesosOros(ListaBathmoi)


    choice2 = input("Θες να επιστρέψεις στο menu?\n(1) ΝΑΙ (2) ΟΧΙ\n :")
    clear()
    while choice2 not in ["1","2"]:
        choice2 = input("Λάθος επιλογή\nΘες να επιστρέψεις στο menu?\n(1) ΝΑΙ (2) ΟΧΙ\n :")
        clear()