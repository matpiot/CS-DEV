import random
from carte import Carte


class Paquet:
    """
    Représente un paquet complet de 52 cartes.
    """

    def __init__(self):
        """
        Crée toutes les cartes du paquet.
        """

        couleurs = ["coeur", "carreau", "pique", "trefle"]
        valeurs = list(range(2, 15))

        self.cartes = []

        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append(Carte(valeur, couleur))


    def melanger(self):
        """
        Mélange les cartes du paquet.
        """

        random.shuffle(self.cartes)


    def distribuer(self):
        """
        Coupe le paquet en deux pour distribuer aux joueurs.
        """

        milieu = len(self.cartes) // 2

        return self.cartes[:milieu], self.cartes[milieu:]