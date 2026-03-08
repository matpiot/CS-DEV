"""
Logique de partie Mastermind : gestion du code secret, des tentatives et du score de la manche.
"""
from code_secret import CodeSecret
from tentative import Tentative
from code_secret import CodeSecret
from tentative import Tentative

class Jeu:
    def __init__(self, max_tours=10):
        """
        Entrée : max_tours (int) nombre maximal d'essais autorisés.
        Sortie : None.
        Effet : prépare un code secret, initialise les compteurs de tours et l'état de victoire.
        """
        self.max_tours = max_tours
        self.tentatives = []
        self.code_secret = CodeSecret()
        self.tour_actuel = 0
        self.gagne = False

    def jouer_tentative(self, choix):
        """
        Entrée : choix (liste de str) couleurs proposées par le joueur.
        Sortie : tuple (bien_places, mal_places) ou None si la partie est déjà terminée.
        Effet : crée une tentative, calcule le retour, l'enregistre, incrémente le tour et
        met à jour l'état de victoire si besoin.
        """
        if self.tour_actuel >= self.max_tours or self.gagne:
            return None  # Jeu terminé

        t = Tentative(choix)
        bien_places, mal_places = t.verifier(self.code_secret)
        self.tentatives.append(t)
        self.tour_actuel += 1

        if bien_places == self.code_secret.longueur:
            self.gagne = True

        return bien_places, mal_places