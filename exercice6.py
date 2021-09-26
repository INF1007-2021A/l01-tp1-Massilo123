import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):

    module = math.sqrt((nombreComplexe.real)**2 + (nombreComplexe.imag)**2)

    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    print("le module du nombre complexe est:",round(module,3),"et l'angle de rotation est:",round(angle,3))


    nombreComplexe1= complex(math.cos(angle),math.sin(angle))
    resultat = nombreComplexe*nombreComplexe1


    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    print("le nouveau module du nombre complexe est:",round(nouveauModule,3),"et le nouvel angle de rotation est:",round(nouvelAngle,3))

    return resultat


def dessiner(number, label):
    ax = plt.subplot(projection='polar')
    if number != None:
        ax.plot([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
