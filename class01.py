import random
import time
import os

def clear():
    os.system("cls")

class Character:
    def __init__(self, name="", health=0):
        self.name = name
        self.health = health
    
    
    def get_values(self, nameChar="χαρακτήρα"):
        print(f"Δώσε στοιχεία {nameChar}")
        self.name = input(f"Δώσε όνομα {nameChar}: ")

        epanal = True
        while epanal:
            try:
                self.health = int(input("Δώσε ζωή: "))

                if self.health < 100 or self.health >500:
                    print("Δεχεται μονο απο 100 - 500")
                else:
                    epanal = False

            except ValueError:
                print("Error 001\nΔέχεται μόνο νούμερα")

    def show_values(self):
        print(f"ΟΝΟΜΑ: {self.name} | ΖΩΗ: {self.health}")
    
    def Pattack(self, target):
        dmg = random.randint(35, 45)
        target.health -= dmg

        if target.health < 0:
            target.health = 0
        
        print(f"⚔️ Ο {self.name} επιτέθηκε στον {target.name} και του έκανε {dmg} damage")
        


player = Character()
player.get_values("παίκτη")

print("-" * 30)

enemy = Character()
enemy.get_values("εχθρού")

clear()

print("\n--- ΣΤΑΤΙΣΤΙΚΑ ---")
player.show_values()
enemy.show_values()

input("\nΠάτα any για να προχωρησης")
clear()

while player.health > 0 and enemy.health > 0:
    
    input("Πάτα any για να επιτεθείς ")
    player.Pattack(enemy)
    enemy.show_values()
    
    if enemy.health <= 0:
        print(f"\n🏆 Ο {player.name} κερδισε")
        break

    print(f"\n🤖 Σειρά του {enemy.name}")
    time.sleep(2)
    enemy.Pattack(player)
    player.show_values()
    
    time.sleep(3)
    clear()

    if player.health <= 0:
        print(f"\n💀 Ο {enemy.name} σε νίκησε \nGame Over")
        break
