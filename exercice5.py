def pointDeRencontre(v1, v2, distance):
    temps=distance/(v1+v2)
    return temps*v2



if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
