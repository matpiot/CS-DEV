import tkinter as tk
from jeu import Jeu

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Space Invaders")
        self.largeur = 600
        self.hauteur = 400
        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="black")
        self.canvas.pack()

        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", pady=4)

        tk.Button(control_frame, text="Jouer", command=self.start).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(control_frame, text="Rejouer", command=self.reset).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(control_frame, text="Quitter", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=2)

        self.score_label = tk.Label(self.root, text="Score : 0", font=("Arial", 14))
        self.score_label.pack(pady=2)

        self.jeu = Jeu(self.canvas, self.largeur, self.hauteur)
        self.running = False

        self.root.bind("<Left>", lambda e: self.jeu.deplacer_vaisseau(-10))
        self.root.bind("<Right>", lambda e: self.jeu.deplacer_vaisseau(10))
        self.root.bind("<space>", lambda e: self.jeu.tirer())

        self.update()

    def update(self):
        if self.running and not self.jeu.game_over:
            self.jeu.mise_a_jour()
            self.score_label.config(text=f"Score : {self.jeu.score}")
            self.root.after(50, self.update)
        elif self.jeu.game_over:
            message = "VICTOIRE" if getattr(self.jeu, "win", False) else "GAME OVER"
            self.canvas.create_text(self.largeur//2, self.hauteur//2, text=message, fill="red", font=("Arial", 40))

    def lancer(self):
        self.root.mainloop()

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def reset(self):
        self.running = False
        self.canvas.delete("all")
        self.jeu = Jeu(self.canvas, self.largeur, self.hauteur)
        self.score_label.config(text="Score : 0")
        self.running = True
        self.update()

if __name__ == "__main__":
    app = Interface()
    app.lancer()