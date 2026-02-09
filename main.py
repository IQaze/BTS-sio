# Programme s'inspirant du jeu Cardline
__authors__ = "Prof"
__version__ = "1.0.0"
__date__ = "2023/02"

from typing import List
import random
from animal import animal
from fonctions_prof import afficherListe, getElemPrecedent, getElemSuivant, getElemInListeAleatoire
def randomANIMAL():
    return animal(getElemInListeAleatoire(animalP), random.randint(1, 10))
# -------------------------------------------------------------------------------------------
# fonction d'affichage et de comparaison
# -------------------------------------------------------------------------------------------
animalP=["Loup","Koala","Panda"]
def choisirPlace(numMax : int) -> int:
    """Permet de choisir la position pour placer la carte en respectant la taille de la liste.
    :param numMax : valeur max de placement possible
    :return: la position choisie
    """
    place = int(input("choisit une place"))
    while place > numMax or place < 0:
        place = int(input("rechoisit une place"))
    return place

def comparer(ani: animal, autreAni: animal) -> bool:
    """Compare ani et autreAni selon la taille.
    :param ani : animal à comparer au second
    :param autreAni : animal à comparer
    :return : Renvoie True si la taille d'ani est plus petite ou égale à celle d'autreAni. False sinon
    """
    #TODO : à implémenter
    pass

def jouerNouvelleCarte() -> str:
    """Permet de proposer de jouer une nouvelle carte O/N
    :return: la réponse : O ou N
    """
    choix = input("Jouer une nouvelle carte : O/N ?")
    while choix != 'O' and choix != 'N':
        choix = input("Jouer une nouvelle carte : O/N ?")
    return choix

def menu():
    """
    Affichage du menu et sélection du choix du joueur
    :return:
    """
    print("Menu : ")
    print("1 - afficher la liste des animaux")
    print("2 - jouer à la classification selon la taille ")
    print("3 - ajouter un nouvel animal ")
    print("9 - quitter")
    choix = int(input("Votre Choix ? : "))
    while choix != 1 and choix != 2 and choix != 3 and choix != 9:
        choix = int(input("Votre Choix ? : "))
    return choix

def testerInsertionAnimal(listeAni : List[animal], pos: int, unAni: animal)-> bool:
    """Permet de vérifier la position pour l'insertion dans une liste
    :param listeAni: liste des animaux ordonnées selon la taille
    :param pos: place proposée pour insérer
    :param unAni: animal
    :return:
        Renvoie True si place est la bonne position pour insérer unAni dans la liste en respectant le critère de taille. False sinon.
    """
    #TODO : à implémenter
    pass

# ----------------------------------------------------------------------------------------------------------------#
# PROGRAMME PRINCIPAL --------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------#

# création des cartes
listeAnimaux = []
#TODO ETAPE 1 : création des animaux

#TODO : initialisation de la pioche (mélangée) et de la cardline(une carte de départ)

print("Bienvenue dans le jeu Cardline : le but consiste à ordonnner les animaux selon une caractéristique : la taille")
choix = menu()
while choix != 9:

    if choix == 1:
        print("DEBUG - Affichage de la liste des cartes à implémenter")
        #TODO ETAPE 1 : affichage de la liste des cartes
        print(listeAnimaux)
    elif choix == 2:
        print("DEBUG - Tour de jeu : placement d'une carte à implémenter")

        #ETAPE2 - partie Niveau 1 : 1 carte à placer par rapport à une carte de cardline
        #TODO ETAPE 2 : création de la cardline
        cardline=[]

        #TODO ETAPE 2 : ajout d'une carte aléatoire à la cardline
        cardline.append(animal(getElemInListeAleatoire(animalP),random.randint(1, 10)))

        #TODO ETAPE 2 : affichage de la cardline
        print (cardline)

        #TODO ETAPE 2 : proposer une carte Animal à jouer, tirée aléatoirement
        Rani=randomANIMAL()
        print("veut tu joue le",Rani)

        #TODO ETAPE 2 : choix du placement par le joueur dans la cardline
        #TODO ETAPE 2 : vérification de la proposition du joueur et affichage du résultat
        place = choisirPlace(len(cardline))
        print("la place ",place," et possible")
        #TODO ETAPE 2 : si OK, ajout à la cardline, sinon defausse de la carte jouée
        ajoutCardline=input('veut tu ajouter au card line ?')
        if ajoutCardline == 'oui':
            cardline.append(Rani)
        #TODO ETAPE 2 : affichage de la cardline
        print (cardline)
        #ETAPE2 - partie Niveau 2 : le joueur peut jouer plusieurs cartes...


    elif choix == 3 :
        #TODO ETAPE 1 : ajout d'un animal à implémenter
        nouveauxANI=animal(input(str()),input(int()))
        listeAnimaux.append(animal)
        print (listeAnimaux)
        print("DEBUG - Ajout d'un nouvel animal à implémenter")

    choix = menu()
