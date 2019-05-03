import pickle


def les_fichiers():
    with open("fichier.txt", "r") as fichier:
        text = fichier.read()
        print(text)
    #fichier.write("\nEt en plus ça marche marche wouah")


def ecrire_objets(_objet):
    
    with open('donnees.txt', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(_objet)
        
def lire_objet(nom_fichier):
    with open(nom_fichier, 'rb') as fichier:
        mon_pickler = pickle.Unpickler(fichier)
        contenu = mon_pickler.load()
        print(contenu)
   


