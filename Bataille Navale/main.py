from jeu import JeuBatailleNavale
from interface import InterfaceJeu


def main():

    jeu = JeuBatailleNavale()

    interface = InterfaceJeu(jeu)

    interface.lancer()


if __name__ == "__main__":
    main()