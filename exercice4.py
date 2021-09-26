import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    duree=duree/3600
    positionInitiale=positionInitiale/1000
    positionFinale = (((vitesseInitiale+vitesseFinale)*duree/2)+positionInitiale)

    return positionFinale*1000

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
