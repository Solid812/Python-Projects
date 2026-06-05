import os 

def clear():
    os.system("cls")

def menu():
    print("/***** Menu *****/")
    print("(1) Εγγραγή\n(2) Συνδεση\n(3) Λογαριασμοί\n(4) Έξοδος")
    choice = input(": ")
    clear()
    while choice not in ["1","2","3","4"]:
        print("/***** Menu *****/")
        print("Λάθος επιλογή\n(1) Εγγραγή\n(2) Συνδεση\n(3) Λογαριασμοί\n(4) Έξοδος")
        choice = input(": ")
        clear()
    return choice

def signUp(onomata , passwords):

    print("/***** Εγγραφή *****/")
    onoma = input("Όνομα χρήστη : ")
    
    if onoma in onomata:
        print("Το όνομα υπάρχει είδη")
    
    else :
        password = input("Κωδικός χρήστη : ")
        onomata.append(onoma)
        passwords.append(password)
        print("Εγγραφή επιτυχής")

def logIn(onomata , passwords):

    prospathies = 3
    for i in range(prospathies):
        print("/***** Σύνδεση *****/")
        onoma = input("Όνομα χρήστη : ")
        password = input("Κωδικός χρήστη : ")
        clear()
        if onoma in onomata:
            index = onomata.index(onoma)
            if passwords[index] == password:
                print("Σύνδεση επιτυχής")
                return

        print(f"Λάθος όνομα χρήστη ή κωδικός\nΣας απομένουν {prospathies - 1 - i} προσπάθιες")

    print("Τελείωσαν οι προσπαθιές σας")

def data(onomata , passwords):

    if not onomata:
        print("Δεν υπάρχουν λογαριασμοί")
        return
    else:
        Scode = "1234"
        prospathies = 3

        for i in range(prospathies):
            print("Εισάγεται κωδικό πρόσβασης")
            code = input(": ")
            if code == Scode:        
                print("/***** Λογαριασμοί *****/")
                for i in range(len(onomata)):
                    print(f"{i+1}ος χρήστης\nΌνομα : {onomata[i]}  |  Κωδικώς : {passwords[i]}")
                print("/***********************/")
                return
            
            print(f"Λάθος κωδικός\nΕισάγεται κωδικό πρόσβασης\nΣας απομένουν {prospathies - 1 - i} προσπάθιες")

    print("Τελείωσαν οι προσπαθιές σας")

def tryAgain():
    print("θέλετε να γυρίσεται πίσω στο menu?\n(1) ΝΑΙ\n(2) ΟΧΙ")
    choice = input(": ")
    return choice

#Main
ListaOnomata = []
ListaPasswords = []

epanalipsi = True
while epanalipsi:
    choice2 = menu()
    clear()

    if choice2 == "1":
        signUp(ListaOnomata , ListaPasswords)
    elif choice2 == "2":    
        logIn(ListaOnomata , ListaPasswords)
    elif choice2 == "3":
        data(ListaOnomata , ListaPasswords)
    elif choice2 == "4":
        epanalipsi = False
        break

    choice = tryAgain()
    clear()
    if choice == "2":
        epanalipsi = False
