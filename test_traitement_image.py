import numpy as np
from traitement_image import appliquer_transformation_1
from traitement_image import appliquer_transformation_2
def test_appliquer_transformation_1_a():
    # Tableau NumPy fourni
    image_gris = np.array([[2, 5, 3, 9, 15],
                           [6, 7, 9, 1, 5],
                           [3, 8, 4, 2, 9],
                           [2, 3, 5, 8, 2],
                           [1, 2, 3, 2, 1]])

    # Tableau NumPy attendu en sortie
    resultat_attendu = np.array([[0, 0, 0, 0, 0],
                                 [0, 20, 32, 255, 0],
                                 [0, 32, 205, 191, 0],
                                 [0, 248, 144, 32, 0],
                                 [0, 0, 0, 0, 0]], dtype=np.uint8)

    # Appel de la fonction à tester
    resultat_obtenu = appliquer_transformation_1(image_gris)

    # Vérification en utilisant assert
    assert np.array_equal(resultat_attendu, resultat_obtenu)

def test_appliquer_transformation_1_b():
    # Tableau NumPy fourni
    image_gris = np.array([[88, 20, 56, 49, 145, 123],
                           [60, 17, 99, 121, 55, 56],
                           [80, 8, 45, 100, 99, 30],
                           [255, 23, 155, 88, 12, 78],
                           [100, 200, 23, 82, 155, 254]])

    # Tableau NumPy attendu en sortie
    resultat_attendu = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 251, 24, 32, 119, 0],
                                 [0, 255, 124, 66, 129, 0],
                                 [0, 191, 2, 105, 255, 0],
                                 [0, 0, 0, 0, 0, 0]], dtype=np.uint8)

    # Appel de la fonction à tester
    resultat_obtenu = appliquer_transformation_1(image_gris)

    # Vérification en utilisant assert
    assert np.array_equal(resultat_attendu, resultat_obtenu)

def test_appliquer_transformation_2_a():

    image_gris = np.array([[88, 102, 133, 49, 145, 123],
                           [14, 100, 200, 121, 55, 56],
                           [40, 101, 92, 100, 99, 30],
                           [255, 23, 155, 88, 12, 78],
                           [100, 200, 23, 82, 155, 254]])

    # Tableau NumPy attendu en sortie
    resultat_attendu = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 3, 6, 3, 6, 0],
                                 [0, 6, 5, 3, 5, 0],
                                 [0, 7, 5, 3, 6, 0],
                                 [0, 0, 0, 0, 0, 0]], dtype=np.uint8)

    # Appel de la fonction à tester
    resultat_obtenu = appliquer_transformation_2(image_gris, 1)

    # Vérification en utilisant assert
    assert np.array_equal(resultat_attendu, resultat_obtenu)

def test_appliquer_transformation_2_b():

    image_gris = np.array([[88, 102, 133, 49, 145, 123],
                           [14, 100, 200, 121, 55, 56],
                           [40, 101, 92, 100, 99, 30],
                           [255, 23, 155, 88, 12, 78],
                           [100, 200, 23, 82, 155, 254]])

    # Tableau NumPy attendu en sortie
    resultat_attendu = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0],
                                 [0, 0, 4, 5, 0, 0],
                                 [0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0]], dtype=np.uint8)

    # Appel de la fonction à tester
    resultat_obtenu = appliquer_transformation_2(image_gris, 2)

    # Vérification en utilisant assert
    assert np.array_equal(resultat_attendu, resultat_obtenu)
