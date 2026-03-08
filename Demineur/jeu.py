from grille import Grille


class JeuDemineur:
    """
    Gère la logique du jeu.
    """

    def __init__(self):
        self.grille = Grille()
        self.perdu = False

    def jouer(self):

        while not self.perdu:

            self.grille.afficher()

            x = int(input("Ligne : "))
            y = int(input("Colonne : "))

            mine = self.grille.reveler_case(x, y)

            if mine:
                self.perdu = True
                print("BOOM ! Vous avez perdu.")

        self.grille.afficher()