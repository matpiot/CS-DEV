"""
Représentation d'une tentative de combinaison et logique de comparaison avec le code secret.
"""


class Tentative:
    def __init__(self, choix):
        """
        Entrée : choix (liste[str]) couleurs proposées par le joueur.
        Sortie : None.
        Effet : stocke la proposition et initialise les compteurs de retour.
        """
        self.choix = choix
        self.bien_places = 0
        self.mal_places = 0

    def verifier(self, code_secret):
        """
        Entrée : code_secret (CodeSecret) référence du code à comparer.
        Sortie : tuple (bien_places, mal_places).
        Effet : calcule les pions bien/mal placés, met à jour les attributs de l'objet.
        Note : remplace temporairement dans `self.choix` les bien placés par None pour éviter de les recompter.
        """
        code = code_secret.code.copy()
        self.bien_places = 0
        self.mal_places = 0

        # Vérification des bien placés
        for i in range(len(self.choix)):
            if self.choix[i] == code[i]:
                self.bien_places += 1
                code[i] = None  # On marque comme traité
                self.choix[i] = None

        # Vérification des mal placés
        for c in self.choix:
            if c and c in code:
                self.mal_places += 1
                code[code.index(c)] = None

        return self.bien_places, self.mal_places