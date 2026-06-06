def menu():
    while True:
        print("***** MENU *****")
        choice = input ("(1) Eisagogi bathmon \n(2) Ipologismos \n(3) Exit \n: ")

        if choice not in ['1', '2', '3']:
            print("Apo 1 - 3")
        else :
            return choice


def apothikeusi_se_txt(Lista_bathmoi):
    with open("bathmoi.txt", "w", encoding= "utf-8") as arxeio:
        for bathmos in Lista_bathmoi:
            arxeio.write(f"{bathmos}\n")


def fortosiArxeiou():
    Lista = []
    try:
        with open("bathmoi.txt", "r", encoding= "utf-8") as arxeio:
            for line in arxeio:
                if line.strip():
                    Lista.append(int(grammi.strip()))
        print("fortothikan oi bathmoi sto arxeio")
    except FileNotFoundError:
        print("Error, den brethike to arxeio")
        pass

    return Lista


def eisagogi(Lista_bathmoi) :
    while True :
        try :
            print("***** Eisagogi bathmon *****")
            print("(Apo 0 - 20)")
            bathmos = int(input("Eisagete bathmo : "))

            if bathmos < 0 or bathmos > 20:
                print("Kseperasate ta oria\n")
            else :
                Lista_bathmoi.append(bathmos)

                choice = input("Thelete epipleon eisagogi? \n(Any) NAI (0) OXI \n: ")
                if choice == '0':
                    apothikeusi_se_txt(Lista_bathmoi)
                    return

        except ValueError:
            print("Dexete mono arithmous")


def ipologismos():
    if not Lista_bathmoi:
        print("Den iparxoun kataxorisis")
        return
    else :
        while True:
            print("***** Ipologismos *****")
            choice = input("(1) Mesos oros (2) Megistos (3) Elaxistos (4) Taksinomisi (5) Exit \n: ")

            if choice == '5':
                return
            elif choice not in ['1' ,'2', '3', '4', '5']:
                print("Apo 1 - 4")
            else :
                if choice == '1':
                    mesosOros(Lista_bathmoi)
                elif choice == '2':
                    megistos(Lista_bathmoi)
                elif choice == '3':
                    elaxistos(Lista_bathmoi)
                elif choice == '4' :
                    taksinomisi(Lista_bathmoi)


def mesosOros(Lista_bathmoi):
    sum = 0
    counter = 0

    for i in range(len(Lista_bathmoi)):
        sum += Lista_bathmoi[i]
        counter += 1

    mesos = sum / counter

    print("***** Mesos Oros *****")
    print(f"O mesos oros einai : {mesos}")
    input("Press any key to continue")


def megistos(Lista_bathmoi):
    max = Lista_bathmoi[0]
    
    for i in range(len(Lista_bathmoi)):
        if Lista_bathmoi[i] > max:
            max = Lista_bathmoi[i]

    print("***** Megistos *****")
    print(f"O megistos einai : {max}")
    input("Press any key to continue")


def elaxistos(Lista_bathmoi):
    min = Lista_bathmoi[0]

    for i in range(len(Lista_bathmoi)):
        if Lista_bathmoi[i] < min:
            min = Lista_bathmoi[i]

    print("***** Mikroteros *****")
    print(f"O mikroteros einai : {min}")
    input("Press any key to continue")


def taksinomisi(Lista_bathmoi):
    while True:
        print("***** Taksinomisi *****")
        choice = input("Thes (1) Auksousa h (2) Fthinousa \n: ")

        if choice not in ['1', '2']:
            print("1 h 2\n")

        else:
            if choice == '1':
                Lista_bathmoi.sort()

                print("\n***** Taksinomisi (Auksousa) *****")
                print("Oi bathmoi se auksousa seira einai:")

                for i in range(len(Lista_bathmoi)):
                    print(f"{i+1}os Bathmos: {Lista_bathmoi[i]}")
    
            elif choice == '2':
                Lista_bathmoi.sort(reverse = True)

                print("\n***** Taksinomisi (Fthinousa) *****")
                print("Oi bathmoi se fthinousa seira einai:")

                for i in range(len(Lista_bathmoi)):
                    print(f"{i+1}os Bathmos: {Lista_bathmoi[i]}")

            input("Press any key to continue")
            return
    
#main
Lista_bathmoi = fortosiArxeiou()

while True:
    choice = menu()

    if choice == '1':
        eisagogi(Lista_bathmoi)
    elif choice == '2':
        ipologismos()
    else :
        break
