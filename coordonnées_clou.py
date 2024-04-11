def calculer_coordonnees_clou(A, B, C, D, E):

    """
      Calcule les coordonnées des points d'un assemblage de clouage.

      Arguments :
          A (float): Description de l'élément A.
          B (float): Description de l'élément B.
          C (float): Description de l'élément C.
          D (float): Description de l'élément D.
          E (float): Description de l'élément E.

      Retourne :
          list: Liste des coordonnées des points.

      Exemple d'utilisation :
          points = calculer_coordonnees_clou(10, 5, 3, 2, 4)
      """

    # Calcul des coordonnées des points
    pt_0 = (-B/2, C/2)
    pt_1 = (-B/2, -C/2)
    pt_2 = (-B/2 - D, -A/2)
    pt_3 = (-B/2 - D, A/2)
    pk_0 = (B/2 + E, 0)
    pk_1 = (B/2, -C/2)
    pk_2 = (B/2, C/2)

    # Création de la liste des points avec leurs noms

    points = [
        ("pt_0", pt_0),
        ("pt_1", pt_1),
        ("pt_2", pt_2),
        ("pt_3", pt_3),
        ("pk_2", pk_2),
        ("pk_0", pk_0),
        ("pk_1", pk_1)
    ]

    return points


from transformation_geometrique import calculer_reflexion_point
from transformation_geometrique import calculer_rotate_point
from transformation_geometrique import calculer_inclinaison_point

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation,
                                 direction_inclinaison, angle_inclinaison, axe_reflexion):
                                     
     """
       Applique différentes transformations géométriques à un clou.

       Cette fonction prend en entrée une liste de points qui nous indiquent la  position du clou dans l'espace ainsi
       que les paramètres pour effectuer de transformations géométriques telles que la réflexion, la rotation et
       l'inclinaison. Elle applique ensuite ce transformations aux points et retourne les coordonnées des
       points après chaque transformation.

       Arguments :
           points_clou (list): Liste des points de clouage, chaque élément étant un tuple contenant le nom du point et
           ses coordonnées sous la forme (x, y).
           center_rotation (tuple): Coordonnées du centre de rotation sous forme de tuple (x, y).
           angle_rotation (float): Angle de rotation en degrés.
           direction_inclinaison (str): Direction de l'inclinaison, 'horizontal' ou 'vertical'.
           angle_inclinaison (float): Angle d'inclinaison en degrés.
           axe_reflexion (str): Axe de réflexion, 'x' ou 'y'.

       Retourne :
           tuple: Un tuple contenant trois listes de tuples, chacune représentant les coordonnées des points du clou
                  après chaque transformation. Les listes correspondent respectivement à la réflexion, la rotation et
                  l'inclinaison.

       Exemple d'utilisation :
           reflexion, rotation, inclinaison = appliquer_transformation_clou(points_clou, (0, 0), 90, 'vertical', 45, 'y')
       """
                                     
    # initialisation de listes vides qui contiendront les tuples de coordonées des points
    # après les transformations géométriques
    coord_point_reflexion = []

    coord_point_rotation = []

    coord_point_cisaillement = []

    # application des transformations géométriques aux points du clou
    for i in range(len(points_clou)):
        coord_point_reflexion.append((points_clou[i][0], calculer_reflexion_point((points_clou[i][1]), axe_reflexion)))
        coord_point_rotation.append((points_clou[i][0], calculer_rotate_point((points_clou[i][1]),
                                                                              angle_rotation, center_rotation)))
        coord_point_cisaillement.append((points_clou[i][0], calculer_inclinaison_point((points_clou[i][1]),
                                                                                       angle_inclinaison,
                                                                                       direction_inclinaison)))

    return coord_point_reflexion, coord_point_rotation, coord_point_cisaillement



