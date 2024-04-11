from PIL import Image
import numpy as np

def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):
    
"""
     Convertit une image couleur en niveaux de gris.

     Arguments:
         chemin_image_couleur (str): Le chemin vers l'image couleur.
         chemin_sauvegarde_gris (str): Le chemin pour sauvegarder l'image en niveaux de gris.

     Retourne:
         None: Cette fonction ne retourne rien, elle sauvegarde simplement l'image en niveaux de gris.
     """

    # Ouvrir l'image en couleur
    image_couleur = Image.open(chemin_image_couleur)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image_couleur.size

    # Créer une nouvelle image en niveaux de gris
    image_gris = Image.new('RGB', (largeur, hauteur))

    # Parcourir chaque pixel de l'image en couleur
    for y in range(hauteur):
        for x in range(largeur):
            # Obtenir la couleur du pixel en RGB
            r, g, b = image_couleur.getpixel((x, y))

            # Calculer la moyenne des composantes rouge, verte et bleue
            moyenne = (r + g + b) // 3

            # Créer une couleur grise avec cette moyenne
            couleur_grise = (moyenne, moyenne, moyenne)

            # Définir la couleur du pixel dans l'image en niveaux de gris
            image_gris.putpixel((x, y), couleur_grise)

    # Sauvegarder l'image en niveaux de gris
    image_gris.save(chemin_sauvegarde_gris)

def appliquer_transformation_1(image_gris):

    """
        Applique une transformation à une image en niveaux de gris en utilisant un algorithme de comparaison avec les voisins.

        Cette fonction parcourt chaque pixel de l'image et compare sa valeur avec celle de ses voisins. En fonction de ces
        comparaisons, un code binaire est généré pour chaque pixel. Ce code binaire est ensuite converti en décimal et
        assigné comme valeur du pixel dans l'image transformée.

        Arguments:
            image_gris (numpy.ndarray): L'image en niveaux de gris sous forme de tableau numpy.

        Retourne:
            numpy.ndarray: L'image transformée après l'application de la transformation.
        """

    hauteur, largeur = image_gris.shape
    image_transformee = np.zeros((hauteur, largeur), dtype=np.uint8)

    for y in range(1, hauteur - 1):
        for x in range(1, largeur - 1):
            # Extraire les valeurs des voisins
            voisins = [
                image_gris[y - 1, x - 1], image_gris[y - 1, x], image_gris[y - 1, x + 1],
                image_gris[y, x + 1], image_gris[y + 1, x + 1],
                image_gris[y + 1, x], image_gris[y + 1, x - 1], image_gris[y, x - 1]
            ]

            # Comparer la valeur du pixel à celle de ses voisins
            code_binaire = ''.join('1' if voisin >= image_gris[y, x] else '0' for voisin in voisins)

            # Transformer le code binaire en décimal
            code_decimal = int(code_binaire, 2)

            # Ajouter la valeur décimale dans le tableau à retourner
            image_transformee[y, x] = code_decimal

    return image_transformee

def appliquer_transformation_2(image_gris, rayon):

    """
       Applique une transformation à une image en niveaux de gris en utilisant un voisinage défini par un rayon.

       Cette fonction parcourt chaque pixel de l'image et calcule une valeur de sortie en fonction des valeurs de ses voisins
       dans un voisinage défini par un rayon. Les valeurs de sortie sont calculées en appliquant une opération basée sur les
       différences de valeurs entre les pixels voisins et le pixel en question, suivie d'une transformation logarithmique.

       Arguments:
           image_gris (numpy.ndarray): L'image en niveaux de gris sous forme de tableau numpy.
           rayon (int): Le rayon pour le voisinage utilisé dans la transformation. Plus le rayon est grand, plus la zone
               de voisinage est large.

       Retourne:
           numpy.ndarray: L'image transformée après l'application de la transformation.
       """
    
    # Dimensions de l'image
    hauteur, largeur = image_gris.shape

    # Création d'un tableau pour stocker le résultat de la transformation
    resultat = np.zeros((hauteur, largeur), dtype=np.float32)

    # Parcours de chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # Vérification si le pixel est à l'intérieur des bords
            if rayon <= x < largeur - rayon and rayon <= y < hauteur - rayon:
                # Calcul des valeurs pour chaque voisin
                voisinages = [
                    np.abs(image_gris[y, x + rayon]) - 2 * image_gris[y, x] + np.abs(image_gris[y, x - rayon]),
                    np.abs(image_gris[y + rayon, x]) - 2 * image_gris[y, x] + np.abs(image_gris[y - rayon, x]),
                    np.abs(image_gris[y - rayon, x + rayon]) - 2 * image_gris[y, x] + np.abs(
                        image_gris[y + rayon, x - rayon])
                ]

                # Calcul de la valeur de sortie pour le pixel
                resultat[y, x] = np.log10(1 + sum(voisinages))

    # Remplacement des valeurs des pixels de bord par zéro
    resultat[:rayon, :] = 0
    resultat[-rayon:, :] = 0
    resultat[:, :rayon] = 0
    resultat[:, -rayon:] = 0

    # Conversion de la matrice résultante de float à int
    resultat = resultat.astype(np.uint8)

    return resultat
