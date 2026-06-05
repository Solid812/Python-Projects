
def login():
    menu1()
    username = input("Ονομα χρηστη : ")
    password = input("Κωδικος χρηστη : ")
    menu2()
    found = False

    try:
        with open("ermis.txt" , "r") as file:
            for line in file:
                storedUser , storedPass = line.strip().split(",")
                if username == storedUser and password == storedPass:
                    found = True
                    break
    except FileNotFoundError :
        print("Error , File not found.")
        return

    if found :
        print("Login succesful.")
    else :
        print("Invalid password.")

def menu1():
    print("/***** Sign in *****/")

def menu2():
    print("*********************")

#   Main

login()
