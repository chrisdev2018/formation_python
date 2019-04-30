from random import randrange
from math import ceil
import os


#def tour():
cagnote = int(input("Votre cagnote de départ : "))
mise = int(input("\nVeuillez saisir votre mise : "))
cagnote -= mise

choix = int(input("\nVeuillez choisir votre numero : "))

num_gagnant = randrange(50)
os.system("pause")
print("\nLe numero gagnant est :", num_gagnant)

if choix == num_gagnant:
    mise += 3 * mise
    cagnote += ceil(mise) 
    print("\nBravo!!!!! Vous avez gagne...")
else:
    if (choix % 2 == 0 and num_gagnant % 2 == 0) or (choix % 2 != 0 and num_gagnant % 2 != 0):
        mise += 0.5 * mise
        cagnote += ceil(mise)
        print("\nVous n'avez pas demerite vous gagne les 50%")
    else:
        cagnote += 0 
        print("\nDesole veuillez reessayer une autre fois")

        
print("\nVotre nouvelle cagnote est :", cagnote)  
os.system("pause")       