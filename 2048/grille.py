import random

class Grille:
    """
    Gère la logique du jeu 2048 : grille, déplacements, fusion et score.
    """

    def __init__(self):
        self.taille = 4
        self.score = 0
        self.grille = [[0]*self.taille for _ in range(self.taille)]

        self.ajouter_tuile()
        self.ajouter_tuile()


    def ajouter_tuile(self):
        """
        Ajoute une tuile 2 ou 4 dans une case vide.
        """

        cases_vides = [
            (i, j)
            for i in range(self.taille)
            for j in range(self.taille)
            if self.grille[i][j] == 0
        ]

        if cases_vides:
            i, j = random.choice(cases_vides)
            # 90% de 2, 10% de 4
            self.grille[i][j] = 4 if random.random() < 0.1 else 2


    def compresser(self, ligne):
        """
        Décale les tuiles vers la gauche.
        """

        nouvelle = [x for x in ligne if x != 0]
        nouvelle += [0]*(self.taille - len(nouvelle))

        return nouvelle


    def fusionner(self, ligne):
        """
        Fusionne les tuiles identiques.
        """

        for i in range(self.taille-1):

            if ligne[i] == ligne[i+1] and ligne[i] != 0:

                ligne[i] *= 2
                ligne[i+1] = 0

                self.score += ligne[i]

        return ligne


    def mouvement_gauche(self):
        """
        Déplace les tuiles vers la gauche. Retourne True si la grille a changé.
        """

        nouvelle_grille = []
        changed = False

        for ligne in self.grille:

            originale = list(ligne)
            ligne = self.compresser(ligne)
            ligne = self.fusionner(ligne)
            ligne = self.compresser(ligne)

            if ligne != originale:
                changed = True

            nouvelle_grille.append(ligne)

        if changed:
            self.grille = nouvelle_grille
            self.ajouter_tuile()

        return changed


    def mouvement_droite(self):

        self.grille = [ligne[::-1] for ligne in self.grille]
        changed = self.mouvement_gauche()
        self.grille = [ligne[::-1] for ligne in self.grille]
        return changed


    def mouvement_haut(self):

        self.grille = list(map(list, zip(*self.grille)))
        changed = self.mouvement_gauche()
        self.grille = list(map(list, zip(*self.grille)))
        return changed


    def mouvement_bas(self):

        self.grille = list(map(list, zip(*self.grille)))
        changed = self.mouvement_droite()
        self.grille = list(map(list, zip(*self.grille)))
        return changed


    def mouvements_possibles(self):
        """
        Vérifie s'il reste au moins un déplacement possible.
        """

        # case vide -> possible
        for ligne in self.grille:
            if 0 in ligne:
                return True

        # fusion possible adjacente (horizontale / verticale)
        for i in range(self.taille):
            for j in range(self.taille):
                if j+1 < self.taille and self.grille[i][j] == self.grille[i][j+1]:
                    return True
                if i+1 < self.taille and self.grille[i][j] == self.grille[i+1][j]:
                    return True

        return False