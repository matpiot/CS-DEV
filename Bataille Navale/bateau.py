class Bateau:
    """Représente un bateau avec ses positions et ses impacts."""

    def __init__(self, positions):
        self.positions = positions
        self.touches = set()

    def recevoir_tir(self, position):
        """Enregistre un tir si la position correspond."""
        if position in self.positions:
            self.touches.add(position)
            return True
        return False

    def est_coule(self):
        """Retourne True si toutes les positions sont touchées."""
        return set(self.positions) == self.touches