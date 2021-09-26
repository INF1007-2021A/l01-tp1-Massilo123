import math
def decomposer(secondes):
        # TODO: Assigner à la variable "annees" le nombre d'années
        annees = (secondes // (60 * 60 * 24 * 365))
        reste_annee = (secondes % (60 * 60 * 24 * 365))
        # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
        semaines = (reste_annee // (60 * 60 * 24 * 7))
        reste_semaine = (reste_annee % (60 * 60 * 24 * 7))
        # TODO: Assigner à la variable "jours" le nombre de jours restants
        jours = (reste_semaine // (60 * 60 * 24))
        reste_jour = (reste_semaine % (60 * 60 * 24))
        # TODO: Assigner à la variable "heures" le nombre d'heures restantes
        heures = (reste_jour // (60 * 60))
        reste_heure = (reste_jour % (60 * 60))
        # TODO: Assigner à la variable "minute" le nombre de minutes restantes
        minutes = (reste_heure // (60))
        reste_minute = (reste_heure % (60))
        # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
        secondes = reste_minute

        # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
        print(annees, semaines, jours, heures, minutes, secondes)

        return (annees, semaines, jours, heures, minutes, secondes)



if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
