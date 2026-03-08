from paquet import Paquet
from joueur import Joueur


class Jeu:
    """
    Classe principale gérant la logique du jeu de la bataille.
    """

    def __init__(self):
        """
        Initialise la partie :
        - crée le paquet
        - mélange
        - distribue aux joueurs
        """

        paquet = Paquet()
        paquet.melanger()

        cartes1, cartes2 = paquet.distribuer()

        self.joueur1 = Joueur("Joueur 1", cartes1)
        self.joueur2 = Joueur("Joueur 2", cartes2)


    def tour(self):
        """
        Exécute un tour de jeu.
        """

        if self.joueur1.a_perdu() or self.joueur2.a_perdu():
            return

        pot = []

        carte1 = self.joueur1.jouer_carte()
        carte2 = self.joueur2.jouer_carte()

        if carte1 is None or carte2 is None:
            return

        pot.extend([carte1, carte2])

        print(self.joueur1.nom, "joue", carte1)
        print(self.joueur2.nom, "joue", carte2)

        if carte1.valeur > carte2.valeur:

            print(self.joueur1.nom, "gagne le tour\n")
            self.joueur1.gagner_cartes(pot)

        elif carte2.valeur > carte1.valeur:

            print(self.joueur2.nom, "gagne le tour\n")
            self.joueur2.gagner_cartes(pot)

        else:
            print("Bataille ! (égalité)\n")
            self.resoudre_bataille(pot)


    def resoudre_bataille(self, pot):
        """
        Gère une bataille (égalité) avec une carte face cachée et une carte face visible.
        """

        while True:

            # Vérifie que chaque joueur a assez de cartes pour continuer (1 cachée + 1 révélée)
            if len(self.joueur1.cartes) < 2:
                pot.extend(self.joueur1.cartes)
                pot.extend(self.joueur2.cartes)
                self.joueur2.cartes = []
                self.joueur1.cartes = []
                self.joueur2.gagner_cartes(pot)
                print(self.joueur2.nom, "remporte la bataille (adversaire à court de cartes)\n")
                return

            if len(self.joueur2.cartes) < 2:
                pot.extend(self.joueur1.cartes)
                pot.extend(self.joueur2.cartes)
                self.joueur1.cartes = []
                self.joueur2.cartes = []
                self.joueur1.gagner_cartes(pot)
                print(self.joueur1.nom, "remporte la bataille (adversaire à court de cartes)\n")
                return

            # Une carte face cachée chacun
            pot.append(self.joueur1.jouer_carte())
            pot.append(self.joueur2.jouer_carte())

            # Carte face visible pour départager
            carte1 = self.joueur1.jouer_carte()
            carte2 = self.joueur2.jouer_carte()
            pot.extend([carte1, carte2])

            print(self.joueur1.nom, "révèle", carte1)
            print(self.joueur2.nom, "révèle", carte2)

            if carte1.valeur > carte2.valeur:
                print(self.joueur1.nom, "gagne la bataille\n")
                self.joueur1.gagner_cartes(pot)
                return

            if carte2.valeur > carte1.valeur:
                print(self.joueur2.nom, "gagne la bataille\n")
                self.joueur2.gagner_cartes(pot)
                return

            print("Nouvelle bataille ! (égalité)\n")


    def jouer(self):
        """
        Lance la partie jusqu'à ce qu'un joueur perde.
        """

        tour = 1

        while not self.joueur1.a_perdu() and not self.joueur2.a_perdu():

            print("------ Tour", tour, "------")

            self.tour()

            tour += 1


        if self.joueur1.a_perdu():
            print(self.joueur2.nom, "gagne la partie !")

        else:
            print(self.joueur1.nom, "gagne la partie !")