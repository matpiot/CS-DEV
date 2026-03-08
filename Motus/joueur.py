class Joueur:
    """Représente un joueur."""

    def __init__(self, nom: str):
        self.nom = nom

    def proposer_mot(self):
        """Demande au joueur de proposer un mot."""
        return input("Propose un mot : ").lower()