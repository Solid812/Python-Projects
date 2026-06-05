import os

def clear(): #cls
    os.system("cls")

def menu(): #Arxiko menu
    while True :
        print("/***** ΒΙΒΛΙΟΘΗΚΗ *****/")
        choice = input("(1) Προσθήκη Βιβλίου\n(2) Εμφανιση όλων των βιβλίων\n(3) Αναζήτηση βιβλίου\n(4) Exit\n:")

        if choice not in ["1", '2', '3', '4']:
            print("Λαθος επιλογη, απο 1-3")
        else :
            return choice
   


def prosthikiBibliou(titloi,authors): #Prosthiki bibliou
    while True:
        print("/***** Προσθηκή Βιβλίου *****/")
        title = input("Τίτλος του βιβλίου : ")
        author = input("Ο συγγραφέας του Βιβλίου : ")
        print("/****************************/\n")

        titloi.append(title)
        authors.append(author)

        choice = input("Θες να δημιουργήσης επιπλέον βιβλίο?\n(Any) ΝΑΙ (0) ΟΧΙ\n:")
        clear()
        if choice == "0":
            return



def emfanisiBiblion(titloi , authors): #emfanisi biblion
    if not titloi:#periptosi opou den brethi biblio
        print("Δεν υπάρχει κάποια καταχώρηση\nΠαρακαλώ εισαγετε πρωτα ενα βιβλιο.")
        return

    else :
        print("/***** Εμφάνιση Βιβλίων *****/")
        for i in range(len(titloi)):            #loopa gia emfanisi olon ton biblion
            print(f"{i+1}o Βιβλίο \nΤίτλος : {titloi[i]} | Συγγραφέας : {authors[i]}")
        print("/****************************/\n")

        input("Πατηστε για να προχωρησετε")
        return    


def anazitisi(titloi , authors): #anazitisi biblion
    if not titloi: #periptosi opou den yparxei biblio
        print("Δεν υπάρχει κάποια καταχώρηση\nΠαρακαλώ εισαγετε πρωτα ενα βιβλιο.")
        return
    
    else :
        while True :
            print("/***** Αναζήτηση Βιβλίων *****/")
            print("Θέλεις βάσει τον τίτλο ή τον συγγραφέα?")
            choice = input("(1) Τίτλος (2) Συγγραφέας (0) Εξοδος\n: ")
            clear()

            if choice == '0':
                return

            elif choice not in ['1', '2']:#frouros
                print("Λαθος επιλογη\n1 η 2\n")

            else :
                if choice == '1':     #periptosi opou o xristis theli na anazitisi basei ton titlο
                    found = False
                    titlos = input("Τίτλος : ")
                    clear()

                    for i in range(len(titloi)):#loopa gia anaziti bibliou basei ton titlo
                        if titlos.lower() == titloi[i].lower():
                            print("Το βιβλίο βρέθηκε επυτυχώς.")
                            print(f"Τίτλος : {titloi[i]}")
                            print(f"Συγγραφέας : {authors[i]}")
                            found = True
                            break
                                                                                    
                    if not found :  #periptosi opou den brethike biblio
                        print("Το βιβλίο δεν βρέθηκε")

                        #epilogi ean theli o xristis na ksanaprospathisi
                        choice1_2 = input("Θελετε να δοκιμάσεται ξανά?\n(Any) ΝΑΙ (0) ΟΧΙ\n: ")
                        if choice1_2 == '0':
                            return 
                    else :
                        #erotisi ston xristi an theli na brei kialo biblio
                        choice1_1 = input("Θέλετε να βρείτε επιπλέον βιβλίο?\n(Any) ΝΑΙ (0) ΟΧΙ\n :")
                        clear()

                        if choice1_1 == '0':
                            return
                        
                elif choice == '2' :#periptosi opou o xristis theli na anazitisi basei ton siggrafea
                    found = False
                    author = input("Συγγραφέας : ")
                    clear()

                    for i in range(len(titloi)):#loopa gia anaziti bibliou basei ton siggrafea
                        if author.lower() == authors[i].lower() :
                            print("Το βιβλίο βρέθηκε επυτυχώς.")
                            print(f"Τίτλος : {titloi[i]}")
                            print(f"Συγγραφέας : {authors[i]}")
                            found = True

                    if not found:    #periptosi opou den brethike to biblio
                        print("Το βιβλίο δεν βρέθηκε")

                        #epilogi ean theli o xristis na ksanaprospathisi
                        choice2_2 = input("Θελετε να δοκιμάσεται ξανά?\n(Any) ΝΑΙ (0) ΟΧΙ\n: ")
                        clear()

                        if choice2_2 == '0':
                            return   

                    else :    #erotisi ston xristi an theli na brei kialo biblio
                        choice2_1 = input("Θέλετε να βρείτε επιπλέον βιβλίο?\n(Any) ΝΑΙ (0) ΟΧΙ\n :")
                        clear()

                        if choice2_1 == '0':
                            return                                             
                    
# Main
listaTitloi = []    #lista gia titlous
listaAuthors = [] #lista gia siggrafees

while True :
    choice = menu()
    clear()

    if choice == '1' :
        prosthikiBibliou(listaTitloi,listaAuthors)
        clear()
    elif choice == '2' :
        emfanisiBiblion(listaTitloi,listaAuthors)
        clear()
    elif choice == '3' :
        anazitisi(listaTitloi,listaAuthors)
        clear()
    elif choice == '4':
        break