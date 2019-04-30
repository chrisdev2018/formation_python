import os


def nb_voyelles():
    cmpt = 0
    nom = input("Veuillez entrer votre nom : ")
    
    for lettre in nom:
        if lettre in "aeiouyAEIOUY":
                cmpt+=1

    print ("votre nom contient",cmpt, "voyelles")    




def table(nb, max=10):

    i = 0
    while i<max:
        print((i+1), "*", nb, "=", (i+1)*nb)
        i+=1

def division(numerateur, denominateur):
        
        try:
                resultat = numerateur / denominateur
        except ValueError:
                print("\nErreurVous n'avez pas saisi de valeur")
                os.system("pause")
        except NameError:
                print("\nErreurLa variable numerateur ou denominateur n'a pas été définie.")
                os.system("pause")
        except TypeError:
                print("\nErreurLa variable numerateur ou denominateur possède un type incompatible avec la division.")
                os.system("pause")
        except ZeroDivisionError:
                print("\nErreurLa variable denominateur est égale à 0.")
                os.system("pause")
        else:
                print("Le resultat de la division est :", resultat)
        
                     

def menu():
        
        sortie = 1  
        
        while sortie != 0:
                os.system("cls")
                print("1. Compter le nombre de voyelles d\'un mot saisie au clavier")
                print("2. Afficher la table de multiplication d\'un nombre saisi au clavier")
                print("3. Effectuer une division avec gestion des exceptions")
                print("")
                choix = int(input("Veuillez selectionner le numero de la fonction a executer :"))
                
                if choix == 1:
                        nb_voyelles()
                        print()
                elif choix == 2:
                        nombre = int(input("Veuillez entrer le nombre vous voulez etablir la table de multiplication :"))
                        table(nombre) 
                        print()   
                
                elif choix == 3:
                        
                        
                        try:
                                numerateur = int(input("Entrer le numerateur de la division : "))
                                denominateur = int(input("Entrer le denominateur de la division : "))
                               
                        except ValueError:
                                print("\nErreur : Vous n'avez pas saisi de valeur\n")
                                os.system("pause")
                         
                                division(numerateur, denominateur)
                              
                            
                sortie = int(input("Appuyer sur 0 pour sortir ou sur tout autre touche pour continuer :"))
                if sortie == 0:
                        input("\nA tres bientôt ... ")
                        break
