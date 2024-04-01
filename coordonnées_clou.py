def calculer_coordonnees_clou(A, B, C, D, E):

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



