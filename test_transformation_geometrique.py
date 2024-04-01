from transformation_geometrique import calculer_reflexion_point
from transformation_geometrique import calculer_inclinaison_point
from transformation_geometrique import calculer_rotate_point

def test_calculer_reflexion_point_1():
    point = (2, 4)
    axe = 'x'
    valeur_attendue = (2, -4)
    resultat = calculer_reflexion_point(point, axe)
    assert resultat == valeur_attendue

def test_calculer_reflexion_point_2():
    point = (2, 4)
    axe = 'y'
    valeur_attendue = (-2, 4)
    resultat = calculer_reflexion_point(point, axe)
    assert resultat == valeur_attendue

def test_calculer_rotate_point():

    point = (2, 4)
    angle = 30
    center = (0, 0)
    valeur_attendue = (-0.27, 4.46)
    resultat = calculer_rotate_point(point, angle, center)
    assert resultat == valeur_attendue

def test_calculer_inclinaison_point_1():
    point = (2, 4)
    angle = 5
    direction = 'x'
    valeur_attendue = (2.35, 4.0)
    resultat = calculer_inclinaison_point(point, angle, direction)
    assert resultat == valeur_attendue

def test_calculer_inclinaison_point_2():
    point = (2, 4)
    angle = 5
    direction = 'y'
    valeur_attendue = (2.0, 4.17)
    resultat = calculer_inclinaison_point(point, angle, direction)
    assert resultat == valeur_attendue
