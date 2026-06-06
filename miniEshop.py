class Product:
    def __init__(self , lista_proionton , lista_timon):
        self.listaProionton = lista_proionton
        self.listaTimon = lista_timon
        self.cart = []
    
    def emf_proionta(self):
        print("-Πατήστε το νούμερο αριστερά απο\nτο προιόν για να το επιλέξεται")
        print("-Αν δεν επιθυμείτε κάποιο προιόν ή επιπλέον, πατήστε '0'.")
        print("-Αν επιθυμείτε πολλά προιόντα, τα επιλέγετε ένα-ένα")
        print("/***** ΠΡΟΙΟΝΤΑ *****/")
        for i in range(len(self.listaProionton)):
            print(f"\n({i+1}) {self.listaProionton[i]} | Τιμή : {self.listaTimon[i]}€")
    
    def kalathi(self):
        print("\n\n/***** ΚΑΛΑΘΙ *****/")
        
        
        while True:
            try:
                choice = int(input(": "))
                if choice == 0:
                    break

                elif 1 <= choice <= len(self.listaProionton):
                    proion = self.listaProionton[choice-1]
                    self.cart.append(proion)
                    print(f"Προστέθηκε το {proion} στο καλάθι")
                else:
                    print("Λάθος αριθμός,ξαναπροσπαθήστε.")
        
            except ValueError:
                print("Δέχεται μόνο αριθμούς")

        print(f"Συνολικά επιλέξατε :")
        for i in range(len(self.cart)):
            print(f"{self.cart[i]}")

#Main
proionta = ["Bananas" , "Apples" , "Potatoes"]
times = [5 , 0.5 , 30]

store = Product(proionta , times)
store.emf_proionta()
store.kalathi()
