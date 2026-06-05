import os

def clear():
    os.system("cls")

def menu():
    print(f"{5 * "*"} Menu {5 * "*"}")

    epanal = True
    while epanal:
        print("(1) Sign In\n(2) Sign Up\n(3)Accounts\n(4) Exit")
        choice = int(input(": "))
        
        if choice not in [1, 2, 3, 4]:
            print("Chose 1 ,2, 3 or 4")
        else:
            return choice

def SignIn(ListUser, ListPassword):
    tries = 3

    epanal = True
    while epanal:
        if tries < 1:
            print("No more tries remaining")
            input("Press any key to continue")
            clear()
            return

        print(f"{5 * "*"} Sign In {5 * "*"}")

        username = input("Username : ")

        password = input("Password : ")

        

        if password not in ListPassword:
            print("Wrong password or username\n")
            choice = input("Do you want to try again or return to menu?\n(Any) YES (0) NO \n:")

            clear()
            tries -= 1

            if tries > 0:
                print(f"You have {tries} tries remaining")

            if choice == "0":
                return
        else :
            epanal = False

    clear()
    print("Epityxhs syndesi")


def SignUp(ListUser , ListPassword):
    print(f"{5 * "*"} Sign Up {5 * "*"}")
    
    epanal = True
    while epanal:
        username = input("Username : ")

        if username in ListUser:
            print("Username already exists")
        else :
            ListUser.append(username)
            epanal = False

    epanal = True
    while epanal:
        print("\nPassword must atleast have 6 characters")
        password = input("Password : ")

        clear()
        
        if len(password) < 6 :
            print("Pasword too short")
        else :
            ListPassword.append(password)
            epanal = False
    clear()
    print("sign up complete")


def data(ListUser, ListPassword):
    if not ListUser:
        print("There are no accounts in the catalogue")
    else:
        for i in range(len(ListUser)):
            print(f"{i + 1}st User \n{ListUser[i]} | {ListPassword[i]}")
    input("Press any key to continue")


#main
ListUser = []
ListPassword = []

epanal = True
while epanal:

    choice = menu()
    clear()

    if choice == 1:
        SignIn(ListUser, ListPassword)
    elif choice == 2:
        SignUp(ListUser , ListPassword)
    elif choice == 3:
        data(ListUser, ListPassword)
        clear()
    else:
        break