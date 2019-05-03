
from fichier import *
from os import system

_dictionnaire = {
    "permier":"tati",
    "deuxieme":"martial",
    "troisieme":"carole"
}

#for cle, valeur in _dictionnaire.items():
#    print("\n cle : {} ; valeur : {}".format(cle, valeur))

ecrire_objets(_dictionnaire) 
lire_objet('donnees.txt') 

    
system('pause')