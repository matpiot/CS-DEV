class Carte:
    """
    Représente une carte de jeu (valeur + couleur).
    """

    def __init__(self, valeur, couleur):
        """
        Initialise une carte.

        paramètres :
            valeur : int (2 à 14)
            couleur : str (coeur, carreau, pique, trefle)
        """
        self.valeur = valeur
        self.couleur = couleur


    def __str__(self):
        """
        Permet d'afficher la carte sous forme lisible.
        """

        noms = {
            11: "Valet",
            12: "Dame",
            13: "Roi",
            14: "As"
        }

        valeur_affichee = noms.get(self.valeur, str(self.valeur))

        return f"{valeur_affichee} de {self.couleur}"