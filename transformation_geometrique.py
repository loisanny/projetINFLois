import math
import numpy as np
def calculer_reflexion_point(point,axe):

    x, y = point

    # Opération si le mirroir est fait selo l'axe x
    if axe == 'x':
        return x, -y

    # Opération si le mirroir est fait selo l'axe y
    elif axe == 'y':
        return -x, y


def calculer_rotate_point(point, angle, center=(0, 0)):

    # initialisation d'une liste qui contient les coordonnées x et y initiales
    coord_point = [point[0], point[1]]

    # initialisation d'une liste qui contiendra la translation à appliquer sur le
    # centre de rotation et le point
    translation_centre = [0]*2

    # initialisation d'un tableau qui contiendra la matrice de rotation
    matrice_rot = np.zeros((2, 2))

    # initialisation d'une liste qui contiendra les coordonnées x et y après la rotation
    coord_point_rot = [0]*2

    # calcul de la translation pour ramener le centre de rotation à l'origine
    # si celui-ci est différent de (0, 0)
    if center != (0, 0):
        translation_centre[0] = 0 - center[0]
        translation_centre[1] = 0 - center[1]

    # application la translation au point si nécessaire
    if translation_centre != [0, 0]:
        coord_point[0] += translation_centre[0]
        coord_point[1] += translation_centre[1]

    # calcul des données de la matrice de transformation
    matrice_rot[0, 0] = math.cos(angle * math.pi / 180)
    matrice_rot[0, 1] = -math.sin(angle * math.pi / 180)
    matrice_rot[1, 0] = math.sin(angle * math.pi / 180)
    matrice_rot[1, 1] = math.cos(angle * math.pi / 180)


    # calcul des coordonnées du point après la rotation
    coord_point_rot[0] = matrice_rot[0, 0] * coord_point[0] + matrice_rot[0, 1] * coord_point[1]
    coord_point_rot[1] = matrice_rot[1, 0] * coord_point[0] + matrice_rot[1, 1] * coord_point[1]

    # application de la translation inverse au point si nécessaire
    if translation_centre != [0, 0]:
        coord_point_rot[0] -= translation_centre[0]
        coord_point_rot[1] -= translation_centre[1]

    # retourner les nouvelles coordonnées du point
    return round(coord_point_rot[0], 2), round(coord_point_rot[1], 2)

calculer_rotate_point((2, 4), 30, (0, 0))

def calculer_inclinaison_point(point, angle, direction):

    # initialisation d'une liste qui contient les coordonnées x et y initiales
    coord_point = [point[0], point[1]]
    # transformer l'angle d'inclinaison en radians
    angle_rad = math.radians(angle)
    # calcul de la tangente de l'angle d'inclinaison
    m = math.tan(angle_rad)

    # initialisation du tableau qui contient la matrice de cisaillement
    matrice_cis = np.array([[1, 0], [0, 1]], dtype = float)

    # initialisation d'une liste qui contiendra les coordonnées x et y après le cisaillement
    coord_point_cis = [0] * 2

    # calcul du cisaillement selon la direction
    if direction == 'x':
        matrice_cis[0,1]=m
        coord_point_cis[0] = matrice_cis[0, 0] * coord_point[0] + matrice_cis[0, 1] * coord_point[1]
        coord_point_cis[1] = matrice_cis[1, 0] * coord_point[0] + matrice_cis[1, 1] * coord_point[1]

    elif direction == 'y':
        matrice_cis[1, 0] = m
        coord_point_cis[0] = matrice_cis[0, 0] * coord_point[0] + matrice_cis[0, 1] * coord_point[1]
        coord_point_cis[1] = matrice_cis[1, 0] * coord_point[0] + matrice_cis[1, 1] * coord_point[1]

    # retourner les nouvelles coordonnées du point
    return round(coord_point_cis[0], 2), round(coord_point_cis[1], 2)
