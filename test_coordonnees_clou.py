from coordonnees_clou import calculer_coordonnees_clou

def test_calculer_coordonnees_clou():

    A = 3
    B = 10
    C = 1
    D = 0.75
    E = 2
    valeur_attendue = [('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2', (-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_2', (5.0, 0.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5))]
    resultat = calculer_coordonnees_clou(A, B, C, D, E)
    assert resultat == valeur_attendue
