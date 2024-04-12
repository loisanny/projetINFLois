import numpy as np


def calculer_histogramme(tableau_2d, w):

    """
        Calcule la distance entre deux histogrammes.

        Cette fonction prend en entrée deux histogrammes et calcule la distance entre eux en utilisant la formule de la
        distance euclidienne.

        Arguments :
            histogramme1 (numpy.ndarray): Le premier histogramme.
            histogramme2 (numpy.ndarray): Le deuxième histogramme.

        Retourne :
            float: La distance entre les deux histogrammes arrondie à deux chiffres après la virgule, ou None si les
                   histogrammes ont des tailles différentes.

        """

    # trouver valeur max du tableau
    valeur_max = tableau_2d.max()

    # déterminer les bins
    bins = [0, int(valeur_max / 4), int(valeur_max / 2), int(3 * valeur_max / 4), valeur_max]

    # initialisation des variables qui contiennent les dimensions du tableau
    largeur, hauteur = tableau_2d.shape

    # initialiser le tableau 2D de l'histogramme
    histogramme = np.zeros(((largeur - 2) * (hauteur - 2), 4), dtype=int)

    # variable ligne du tableau d'histogramme
    i = 0

    # parcourir toutes les données du tableau
    for x in range(w - 2, largeur - (w - 2)):
        for y in range(w - 2, hauteur - (w - 2)):
            # initialisation des limites de la fenêtre
            debut_largeur = x - w + 2
            debut_hauteur = y - w + 2
            fin_largeur = x + w - 2
            fin_hauteur = y + w - 2

            # définition de la fenêtre de l'histogramme
            fenetre = tableau_2d[debut_largeur: fin_largeur + 1, debut_hauteur: fin_hauteur + 1]

            # définition de l'histogramme
            hist, _ = np.histogram(fenetre, bins=bins)
            histogramme[i] = hist

            # incrémenter la ligne du tableau d'histogramme
            i += 1

    return histogramme

def calculer_distance_1(histogramme1, histogramme2):

    """
        Calcule la distance entre deux histogrammes.

        Cette fonction prend en entrée deux histogrammes et calcule la distance entre eux en utilisant la formule de la
        distance euclidienne.

        Arguments :
            histogramme1 (numpy.ndarray): Le premier histogramme.
            histogramme2 (numpy.ndarray): Le deuxième histogramme.

        Retourne :
            float: La distance entre les deux histogrammes arrondie à deux chiffres après la virgule, ou None si les
                   histogrammes ont des tailles différentes.

        """

    # Vérification des tailles des histogrammes
    if len(histogramme1) != len(histogramme2):
        return None

    # Calcul de la distance
    distance_carree = np.sum((histogramme1 - histogramme2) ** 2)
    distance = np.sqrt(distance_carree)

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return distance_arrondie
    

def calculer_distance_2(histogramme1, histogramme2):
    
"""
            Calcule la distance entre deux histogrammes.

            Cette fonction prend en entrée deux histogrammes et calcule la distance entre eux en utilisant la formule de la
            distance de Manhattan.

            Arguments :
                histogramme1 (numpy.ndarray): Le premier histogramme.
                histogramme2 (numpy.ndarray): Le deuxième histogramme.

            Retourne :
                float: La distance entre les deux histogrammes arrondie à deux chiffres après la virgule, ou None si les
                       histogrammes ont des tailles différentes.

            """

    # Vérification des tailles des histogrammes
    if len(histogramme1) != len(histogramme2):
        return None

    # Calcul de la distance
    distance = np.sum(np.abs(histogramme1 - histogramme2))

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return distance_arrondie
