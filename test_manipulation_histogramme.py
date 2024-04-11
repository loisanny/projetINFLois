import numpy as np
from manipulation_histogramme import calculer_histogramme, calculer_distance_1
def test_calculer_histogramme():
    # Tableau NumPy fourni avec w=3
    tableau_fourmi = np.array([[255, 160, 10, 49], [20, 170, 1, 121], [30, 233, 230, 100], [255, 23, 155, 88]])

    # Tableau NumPy attendu
    tableau_attendu = np.array([[4, 0, 2, 3], [3, 2, 2, 2], [4, 0, 2, 3], [2, 3, 2, 2]])

    # Calculer l'histogramme
    resultat = calculer_histogramme(tableau_fourmi, 3)

    # Vérifier si le résultat est égal au tableau attendu
    assert np.array_equal(resultat, tableau_attendu)

def test_calculer_distance1():

    h1_fourni = np.array([1,2,3,4,5])
    h2_fourni = np.array([2,3,4,5,6])

    valeur_attendue = 2.24

    resultat = calculer_distance_1(h1_fourni, h2_fourni)

    assert resultat == valeur_attendue

def test_calculer_distance2():

    h1_fourni = np.array([1, 2, 3, 4, 5])
    h2_fourni = np.array([2, 3, 4, 5, 6])

    valeur_attendue = 5

    resultat = calculer_distance_2(h1_fourni, h2_fourni)

    assert resultat == valeur_attendue
