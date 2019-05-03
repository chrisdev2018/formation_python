import random
import pickle
print("Bienvenue dans la Pharmacie de Cirdo")
 
#-------------------------------------------------------------------------------
#                          Class et Fonction
#-------------------------------------------------------------------------------
 
#Class -------------------------------------------------------------------------
class Client():
  """Client"""
  def __init__(self,credits,nom_client):
    self.credits = credits #Argent du client
    self.nom_clients = nom_client  #Nom du client
 
 
 
  def __str__(self):
    return "{}, tu as {} €".format(self.nom_clients,self.credits)
#Fonction ----------------------------------------------------------------------
def medoc_recupere():
  """Recupere dans un fichier les nom des médoc"""
  with open("medoc.txt","r") as fichier:
    contenu = fichier.read()
  contenu = contenu.split("\n")
  for i,elt in enumerate(contenu):
    if elt is not "":
      elt = elt.split(":")
      elt1 = elt[1].split(",")
      elt1[0] = int(elt1[0])
      elt1[1] = int(elt1[1])
      medicament[elt[0]] = elt1
 
 
 
def client_recpuere():
  """Recupere dans un fichier binaire les clients"""
  client = list()
  try :
    with open("client.bvm","rb") as fichier:
      my_pickle = pickle.Unpickler(fichier)
      client = my_pickle.load()
  except EOFError:
    pass
  except FileNotFoundError:
    pass
  return client
 
 
def affiche_medoc(medicaments):
  """Affiche les medoc"""
  j =0
 
  for i,elt in medicaments.items():
    if j is 0:
      print("Il reste {} {} à {} €,".format(elt[0],i,elt[1]))
    elif j is not 0:
      if j is (len(medicament)-1):
        print("{} {} à {} €.\n".format(elt[0],i,elt[1]))
      else:
        print("{} {} à {} €,".format(elt[0],i,elt[1]))
    j+=1
 
def achat_medoc(client,medoc):
  """Permet l'achat des medoc"""
  boolean_nom = False
  boolean_medoc = False
  id_client = 0
  nom = input("Votre nom de client : ")
  for i,elt in enumerate(client):
    if elt.nom_clients == nom:
        print("Client deja créer")
        boolean_nom = True
        id_client = i
  if boolean_nom is False:
    print("Création du client...")
    client.append(Client(random.randint(0,100),nom))
    print(client[len(client)-1])
    id_client = len(client)-1
  if client[id_client].credits < 0:
    print("Desolez mais vous en deficites...")
  else:
    nom_medoc = input("Nom de médicament : ")
    nb_medoc = 0
    for i,elt in medoc.items():
      if i == nom_medoc:
        boolean_medoc = True
        elt[1] = int(elt[1])
        nb_medoc = elt[1]
 
    if boolean_medoc is False:
      print("Nous avons pas de '{}'.".format(nom_medoc))
    else:
      try :
        nb_q_medoc =int(input("Le nombre de medicament : "))
      except ValueError:
        print("Erreur : Ce ne sont pas des chiffre")
        exit(1)
      if nb_q_medoc > medicament[nom_medoc][0]:
        print("Il n'y a plus asser de {}".format(nom_medoc))
      elif nb_q_medoc*nb_medoc > client[id_client].credits:
        print("Impossible d'effectuer l'achat, il est tros chère")
      else:
        print("Montant du Médicament : {}".format(nb_medoc))
        print("Montant total : {} €".format((nb_q_medoc*nb_medoc)))
        medicament[nom_medoc][0] -=nb_q_medoc
        client[id_client].credits -= (nb_q_medoc*nb_medoc)
        print(client[id_client],"\n")
 
 
def appro(medoc):
  """permet d'approviosement"""
  nom_medoc = input("Nom de médicament : ")
  nb_medoc = 0
  boolean_medoc = False
 
  for i,elt in medoc.items():
    if i == nom_medoc:
      boolean_medoc = True
 
      elt1 = int(elt[1])
      nb_medoc = elt1
      print(nb_medoc)
 
 
 
  if boolean_medoc is False:
    print("Rajout du médicaments : {}".format(nom_medoc))
    medoc[nom_medoc] = int(input("Le prix du nouveau médicaments :  "))
 
  else:
    try :
      nb_q_medoc =int(input("Le nombre de medicament : "))
    except ValueError:
      print("Erreur : Ce ne sont pas des chiffre")
      exit(1)
  medicament[nom_medoc][0] +=nb_q_medoc
 
def enregistrement_medoc(medoc):
  """Fonction qui enregistre les nom des medoc"""
  with open("medoc.txt","w") as fichier:
    for i,elt in medoc.items():
      write_contenu = "{}:{},{}\n".format(i,elt[0],elt[1])
      fichier.write(write_contenu)
def enristrement_client(client):
  """Enrigistre les clients en binaire"""
  with open("client.bvm","wb") as fichier:
    my_pickle = pickle.Pickler(fichier)
    my_pickle.dump(client)
#-------------------------------------------------------------------------------
#                          Programme Principale
#-------------------------------------------------------------------------------
 
client = list() #Liste de tous les clients
 
medicament = dict()
medoc_recupere()
client = client_recpuere()
while 1:
  print("Que vous les vous faire ????")
  choix = input("1 : Achat de medicament\n\
2 : Approvisionnement en  medicaments\n\
3 : Etats des stocks et des credits\n\
4 : Quitter\n")
 
  try :
      choix = int(choix)
  except ValueError:
    print("Erreur : La valeur n'est pas un chiffre")
  if choix is 3:
    affiche_medoc(medicament)
  elif choix is 1:
    achat_medoc(client,medicament)
  elif choix is 2:
    appro(medicament)
  elif choix is 4:
    print("Enregistrement des paramettres...")
    enregistrement_medoc(medicament)
    enristrement_client(client)
    break
 
print("Aurevoir dans la Pharmacie de Cirdo")