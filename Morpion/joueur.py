class Joueur:
    """
    Représente un joueur du morpion.
    """

    def __init__(self, nom, symbole):
        """
        Initialise un joueur.

        paramètres :
            nom : nom du joueur
            symbole : X ou O
        """

        self.nom = nom
        self.symbole = symbole