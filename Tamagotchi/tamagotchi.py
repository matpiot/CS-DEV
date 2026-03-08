class Tamagotchi:
    def __init__(self, nom):
        self.nom = nom
        self.__faim = 50
        self.__energie = 50
        self.__humeur = 50

    # --- Getters ---
    def get_faim(self):
        return self.__faim

    def get_energie(self):
        return self.__energie

    def get_humeur(self):
        return self.__humeur

    # --- Emoji selon humeur ---
    def get_emoji(self):
        if self.__humeur >= 70:
            return "😄"
        elif self.__humeur >= 40:
            return "😐"
        else:
            return "😢"

    # --- Actions ---
    def nourrir(self):
        self.__faim -= 20
        if self.__faim < 0: self.__faim = 0
        self.__humeur += 5
        if self.__humeur > 100: self.__humeur = 100

    def dormir(self):
        self.__energie += 20
        if self.__energie > 100: self.__energie = 100
        self.__humeur += 5
        if self.__humeur > 100: self.__humeur = 100

    def jouer(self):
        self.__humeur += 15
        if self.__humeur > 100: self.__humeur = 100
        self.__energie -= 10
        if self.__energie < 0: self.__energie = 0
        self.__faim += 10
        if self.__faim > 100: self.__faim = 100

    # --- Évolution naturelle ---
    def passer_tour(self):
        self.__faim += 5
        if self.__faim > 100: self.__faim = 100
        self.__energie -= 5
        if self.__energie < 0: self.__energie = 0
        self.__humeur -= 5
        if self.__humeur < 0: self.__humeur = 0

    # --- Vérifier état critique ---
    def est_vivant(self):
        return self.__energie > 0 and self.__faim < 100 and self.__humeur > 0