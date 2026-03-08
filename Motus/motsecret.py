class MotSecret:
    """Représente le mot à deviner."""

    def __init__(self, mot: str):
        self.mot = mot.lower()

    def verifier_tentative(self, tentative: str):
        """
        Compare une tentative avec le mot secret.
        Retourne une liste indiquant le résultat pour chaque lettre.
        """
        resultat = []

        for i, lettre in enumerate(tentative):

            if lettre == self.mot[i]:
                resultat.append("VERT")

            elif lettre in self.mot:
                resultat.append("JAUNE")

            else:
                resultat.append("GRIS")

        return resultat

    def est_trouve(self, tentative: str) -> bool:
        """Vérifie si le mot est trouvé."""
        return tentative == self.mot