from biblioteque import *

_dictionnaire = {
    "permier":"tati",
    "deuxieme":"martial",
    "troisieme":"carole"
}

for cle, valeur in _dictionnaire.items():
    print("\n cle : {} ; valeur : {}".format(cle, valeur))
system('pause')