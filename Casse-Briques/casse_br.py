import tkinter as tk
import random

class Balle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 250
        self.y = 250
        self.vx = 2
        self.vy = 2
        self.balle_objet = canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="blue")

    def deplacer(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= 480:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= 480:
            self.vy = -self.vy

        self.canvas.move(self.balle_objet, self.vx, self.vy)

class Jeu:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de la Balle")

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        self.balle = Balle(self.canvas)

        # Supprimer l'appel direct à self.jouer()
        # self.jouer()  # Retiré pour attendre le clic sur le bouton "Jouer"

        # Ajouter un état pour savoir si le jeu est en cours
        self.jeu_en_cours = False

        self.bouton_jouer = tk.Button(root, text="Jouer", command=self.jouer)
        self.bouton_jouer.pack()

    def jouer(self):
        if not self.jeu_en_cours:
            self.jeu_en_cours = True  # Démarrer le jeu uniquement après le clic sur "Jouer"

        self.balle.deplacer()
        # Relancer la boucle
        self.root.after(10, self.jouer)

if __name__ == "__main__":
    root = tk.Tk()
    jeu = Jeu(root)
    root.mainloop()