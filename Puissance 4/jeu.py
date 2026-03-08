from grille import Grille
from joueur import Joueur


class JeuPuissance4:
    """
    Gère la logique du jeu.
    """

    def __init__(self):

        self.grille = Grille()

        self.joueur1 = Joueur("Joueur 1", "X")
        self.joueur2 = Joueur("Joueur 2", "O")

        self.joueur_actuel = self.joueur1

    def changer_joueur(self):

        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1

    def jouer(self):

        while True:

            self.grille.afficher()

            colonne = self.joueur_actuel.choisir_colonne()

            if not self.grille.colonne_valide(colonne):
                print("Colonne pleine.")
                continue

            self.grille.placer_jeton(colonne, self.joueur_actuel.symbole)

            if self.grille.verifier_victoire(self.joueur_actuel.symbole):

                self.grille.afficher()
                print(f"{self.joueur_actuel.nom} gagne !")
                break

            self.changer_joueur()