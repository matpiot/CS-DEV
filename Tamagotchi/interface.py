import tkinter as tk
from tamagotchi import Tamagotchi

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tamagotchi Amélioré")
        self.tama = Tamagotchi("Tama")
        self.running = True  # les états évoluent même sans interaction

        # Emoji humeur
        self.label_emoji = tk.Label(self.root, text=self.tama.get_emoji(), font=("Arial", 50))
        self.label_emoji.pack(pady=10)

        # Barres graphiques
        self.frame_bars = tk.Frame(self.root)
        self.frame_bars.pack(pady=10)
        self.bar_faim = tk.Canvas(self.frame_bars, width=200, height=20, bg="lightgray")
        self.bar_faim.pack(pady=5)
        self.bar_faim.create_text(0, 10, anchor="w", text="Faim", font=("Arial", 10, "bold"))

        self.bar_energie = tk.Canvas(self.frame_bars, width=200, height=20, bg="lightgray")
        self.bar_energie.pack(pady=5)
        self.bar_energie.create_text(0, 10, anchor="w", text="Énergie", font=("Arial", 10, "bold"))

        self.bar_humeur = tk.Canvas(self.frame_bars, width=200, height=20, bg="lightgray")
        self.bar_humeur.pack(pady=5)
        self.bar_humeur.create_text(0, 10, anchor="w", text="Humeur", font=("Arial", 10, "bold"))

        # Boutons actions
        self.frame_btns = tk.Frame(self.root)
        self.frame_btns.pack(pady=10)
        tk.Button(self.frame_btns, text="Nourrir", command=self.nourrir).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_btns, text="Dormir", command=self.dormir).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_btns, text="Jouer", command=self.jouer).pack(side=tk.LEFT, padx=5)

        # Contrôles de partie
        self.frame_ctrl = tk.Frame(self.root)
        self.frame_ctrl.pack(pady=5)
        tk.Button(self.frame_ctrl, text="Lancer", command=self.lancer_partie).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_ctrl, text="Pause", command=self.pause_partie).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_ctrl, text="Recommencer", command=self.reset_partie).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_ctrl, text="Quitter", command=self.root.destroy).pack(side=tk.LEFT, padx=5)

        # Alertes texte
        self.label_alert = tk.Label(self.root, text="", font=("Arial", 14), fg="red")
        self.label_alert.pack(pady=5)

        self.update()

    def update_bars(self):
        # Redimension des barres selon valeur / 100
        self.bar_faim.delete("all")
        self.bar_energie.delete("all")
        self.bar_humeur.delete("all")
        self.bar_faim.create_text(0, 10, anchor="w", text="Faim", font=("Arial", 10, "bold"))
        self.bar_faim.create_rectangle(40, 0, 40 + 1.6*self.tama.get_faim(), 20, fill="red")

        self.bar_energie.create_text(0, 10, anchor="w", text="Énergie", font=("Arial", 10, "bold"))
        self.bar_energie.create_rectangle(60, 0, 60 + 1.4*self.tama.get_energie(), 20, fill="green")

        self.bar_humeur.create_text(0, 10, anchor="w", text="Humeur", font=("Arial", 10, "bold"))
        self.bar_humeur.create_rectangle(55, 0, 55 + 1.45*self.tama.get_humeur(), 20, fill="yellow")

    def update_labels(self):
        self.label_emoji.config(text=self.tama.get_emoji())

        # Alertes critiques
        alert_msg = ""
        if self.tama.get_faim() >= 80:
            alert_msg += "J'ai faim ! "
        if self.tama.get_energie() <= 20:
            alert_msg += "Je suis fatigué ! "
        if self.tama.get_humeur() <= 20:
            alert_msg += "Je suis triste ! "
        self.label_alert.config(text=alert_msg)

    def nourrir(self):
        self.tama.nourrir()
        self.update_bars()
        self.update_labels()

    def dormir(self):
        self.tama.dormir()
        self.update_bars()
        self.update_labels()

    def jouer(self):
        self.tama.jouer()
        self.update_bars()
        self.update_labels()

    def update(self):
        if self.running and self.tama.est_vivant():
            self.tama.passer_tour()
            self.update_bars()
            self.update_labels()
        elif not self.tama.est_vivant():
            self.label_alert.config(text="Votre Tamagotchi est mort 😢")
            self.label_emoji.config(text="💀")
            self.running = False

        # on reprogramme toujours pour que l'état continue d'évoluer dès qu'on relance
        self.root.after(1000, self.update)

    def lancer(self):
        self.root.mainloop()

    def lancer_partie(self):
        if self.tama.est_vivant():
            self.running = True

    def pause_partie(self):
        self.running = False

    def reset_partie(self):
        self.running = True
        self.tama = Tamagotchi("Tama")
        self.label_alert.config(text="")
        self.label_emoji.config(text=self.tama.get_emoji())
        self.update_bars()
        self.update_labels()

if __name__ == "__main__":
    app = Interface()
    app.lancer()