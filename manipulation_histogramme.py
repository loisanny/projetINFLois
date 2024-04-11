import numpy as np


def calculer_histogramme(tableau_2D, w):
    max_value = np.max(tableau_2D)
    bins = [0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value]
    nb_lignes, nb_colonnes = tableau_2D.shape
    histogrammes = np.zeros((nb_lignes - w + 1, nb_colonnes - w + 1, len(bins) - 1), dtype=int)

    for i in range(nb_lignes - w + 1):
        for j in range(nb_colonnes - w + 1):
            debut_i = i
            fin_i = i + w
            debut_j = j
            fin_j = j + w

            fenetre = tableau_2D[debut_i:fin_i, debut_j:fin_j]
            hist, _ = np.histogram(fenetre, bins=bins, range=(0, max_value))
            # Assurer que la forme de l'histogramme créé correspond à celle de histogrammes
            histogrammes[i, j] = hist[:-1]


    return histogrammes

def calculer_distance_1(histogramme1, histogramme2):

    # Vérification des tailles des histogrammes
    if len(histogramme1) != len(histogramme2):
        return None

    # Calcul de la distance
    distance_carree = np.sum((histogramme1 - histogramme2) ** 2)
    distance = np.sqrt(distance_carree)

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie = round(distance, 2)

    return distance_arrondie
