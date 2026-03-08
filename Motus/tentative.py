from motsecret import MotSecret


class Tentative:
    """Représente une tentative d'un joueur."""

    def __init__(self, mot_propose: str):
        self.mot_propose = mot_propose.lower()
        self.resultat = []

    def evaluer(self, mot_secret: MotSecret):
        """Évalue la tentative par rapport au mot secret."""
        self.resultat = mot_secret.verifier_tentative(self.mot_propose)

    def afficher(self):
        """Affiche le résultat de la tentative."""
        affichage = ""

        for lettre, statut in zip(self.mot_propose, self.resultat):
            if statut == "VERT":
                affichage += f"[{lettre}]"
            elif statut == "JAUNE":
                affichage += f"({lettre})"
            else:
                affichage += f" {lettre} "

        print(affichage)