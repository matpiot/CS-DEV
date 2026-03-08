"""
Gestion du code secret du Mastermind : génération et représentation du code caché.
"""

import random


class CodeSecret:
    def __init__(self, couleurs=None, longueur=4):
        """
        Entrée :
            couleurs (liste[str] | None) palette disponible, défaut : 6 couleurs.
            longueur (int) nombre de pions du code.
        Sortie : None.
        Effet : construit un code secret aléatoire et mémorise la palette/longueur.
        """
        if couleurs is None:
            couleurs = ["rouge", "bleu", "vert", "jaune", "orange", "violet"]
        self.couleurs = couleurs
        self.longueur = longueur
        self.code = self.generer_code()

    def generer_code(self):
        """
        Entrée : aucune.
        Sortie : liste[str] représentant le code secret généré.
        Effet : crée un nouveau code aléatoire à partir de la palette.
        """
        return [random.choice(self.couleurs) for _ in range(self.longueur)]

    def __repr__(self):
        """
        Entrée : aucune.
        Sortie : str lisible du code secret.
        Effet : facilite l'affichage/logging.
        """
        return f"<CodeSecret {self.code}>"