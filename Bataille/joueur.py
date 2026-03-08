class Joueur:
    """
    Représente un joueur possédant un tas de cartes.
    """

    def __init__(self, nom, cartes):
        """
        Initialise le joueur.

        paramètres :
            nom : str
            cartes : liste de cartes
        """

        self.nom = nom
        self.cartes = cartes


    def jouer_carte(self):
        """
        Le joueur joue la première carte de son tas.
        """

        if self.cartes:
            return self.cartes.pop(0)

        return None


    def gagner_cartes(self, cartes):
        """
        Ajoute les cartes gagnées à la fin du tas.
        """

        self.cartes.extend(cartes)


    def a_perdu(self):
        """
        Vérifie si le joueur n'a plus de cartes.
        """

        return len(self.cartes) == 0