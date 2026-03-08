class Joueur:
    """
    Représente un joueur.
    """

    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    def choisir_colonne(self):
        return int(input(f"{self.nom}, choisis une colonne : "))