from os import system

def les_fichiers():
    with open("fichier.txt", "r") as fichier:
        text = fichier.read()
        print(text)
    #fichier.write("\nEt en plus ça marche marche wouah")


les_fichiers()


system("pause")
