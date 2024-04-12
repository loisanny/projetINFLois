import math
import numpy as np

def calculer_reflexion_point(point,axe):
    
 """
    Calcule la réflexion d'un point par rapport à un axe.

    Cette fonction prend en entrée les coordonnées d'un point (x, y) et un axe ('x' ou 'y') et calcule la réflexion
    du point par rapport à cet axe.

    Arguments :
        point (tuple): Les coordonnées du point sous forme de tuple (x, y).
        axe (str): L'axe de réflexion, 'x' pour l'axe horizontal ou 'y' pour l'axe vertical.

    Retourne :
        tuple: Les coordonnées du point réfléchi sous forme de tuple (x, y).
        
    """
    x, y = point

    # Opération si le mirroir est fait selo l'axe x
    if axe == 'x':
        return x, -y

    # Opération si le mirroir est fait selo l'axe y
    elif axe == 'y':
        return -x, y


def calculer_rotate_point(point, angle, center=(0, 0)):

    """
       Calcule la rotation d'un point autour d'un centre donné.

       Cette fonction prend en entrée les coordonnées d'un point (x, y), un angle de rotation en degrés, et éventuellement
       un centre de rotation (par défaut à l'origine), et calcule les nouvelles coordonnées du point après rotation.

       Arguments :
           point (tuple): Les coordonnées du point initial sous forme de tuple (x, y).
           angle (float): L'angle de rotation en degrés.
           center (tuple, optionnel): Les coordonnées du centre de rotation sous forme de tuple (x, y). Par défaut, le
                                      centre de rotation est l'origine (0, 0).

       Retourne :
           tuple: Les coordonnées du point après rotation sous forme de tuple (x, y).
           
       """

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


def calculer_inclinaison_point(point, angle, direction):

        """
    Calcule l'inclinaison d'un point selon une direction donnée.

    Cette fonction prend en entrée les coordonnées d'un point (x, y), un angle d'inclinaison en degrés, et une direction
    ('x' ou 'y'), et calcule les nouvelles coordonnées du point après inclinaison selon cette direction.

    Arguments :
        point (tuple): Les coordonnées du point initial sous forme de tuple (x, y).
        angle (float): L'angle d'inclinaison en degrés.
        direction (str): La direction de l'inclinaison, 'x' pour une inclinaison selon l'axe des abscisses, 'y' pour
                         une inclinaison selon l'axe des ordonnées.

    Retourne :
        tuple: Les coordonnées du point après inclinaison sous forme de tuple (x, y).
        
    """

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
