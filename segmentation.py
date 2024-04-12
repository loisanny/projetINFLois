from manipulation_histogramme import calculer_distance_1
import numpy as np

def regrouper_points(data, k, max_iterations=50):
  
    """
      Divise un ensemble de points dans un plan 2D en un nombre défini de groupes en utilisant l'algorithme de k-moyennes.

      Cette fonction prend en entrée un ensemble de données représenté par un tableau 2D numpy, où chaque ligne du
      tableau représente un histogramme décrivant un point. Elle divise cet ensemble en un nombre spécifié de groupes k
      en utilisant l'algorithme de k-moyennes.

      Arguments :
          data (numpy.ndarray): Un tableau 2D numpy représentant l'ensemble de données à partitionner.
                                Chaque ligne du tableau représente un histogramme décrivant un point.
          k (int): Le nombre de groupes à identifier dans l'ensemble de données.
          max_iterations (int, optionnel): Le nombre maximal d'itérations que l'algorithme exécutera.
                                            La valeur par défaut est 50.

      Retourne :
          numpy.ndarray: Un tableau numpy 1D où chaque élément correspond à l'indice du centre le plus proche pour
                         chaque point de l'ensemble de données. C'est un vecteur d'entiers de la même longueur que le
                         nombre de points dans 'data', indiquant l'affectation de groupe pour chaque point.

      """
  
    # Initialisation des centres de manière aléatoire
    indices = np.random.choice(len(data), k, replace=False)
    centres = data[indices]

    # Initialisation de l'affectation des groupes
    affectations = np.zeros(len(data))

    for _ in range(max_iterations):
        # Assigner chaque point au centre le plus proche
        for i, point in enumerate(data):
            distances = [calculer_distance_1(point, centre) for centre in centres]
            affectations[i] = np.argmin(distances)

        # Mettre à jour les centres en calculant les moyennes des points de chaque groupe
        for j in range(k):
            groupe_points = data[affectations == j]
            if len(groupe_points) > 0:
                centres[j] = np.mean(groupe_points, axis=0)

    return affectations.astype(int)
