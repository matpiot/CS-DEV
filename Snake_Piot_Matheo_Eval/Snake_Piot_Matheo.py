"""
-*- coding: utf-8 -*-

Auteur : Piot Matheo, CPE Lyon, 3ETI-B

Date : 2024-06-10

Description : Implémentation du jeu Snake en utilisant Tkinter pour l'interface graphique. 
Nous utilisons 3 classes : Snake (classe principale), Carré (représente les segments du serpent) 
et Pomme (représente les pommes à manger).
"""

import tkinter as tk
import random as rd
import Pomme
import Carré

class Snake:

    def __init__(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Initialise l'interface Tkinter (fenêtre, canevas, labels, boutons),
            crée les objets du jeu (carrés, pommes) et démarre la boucle
            principale Tkinter (self.root.mainloop()).
        """

        self.root = tk.Tk()
        self.root.title("Snake")
        self.canvas = tk.Canvas(self.root, width = 900, height = 500, bg = "white")
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_score = tk.Label(self.root, text = "Score : 0", fg = 'black', bg = 'white')
        self.label_score.grid(row = 0, column = 0)
        self.bouton_quitter = tk.Button(self.root, text = "Quitter", command = self.root.destroy, fg = 'black', bg = "#FFFFFF")
        self.bouton_quitter.grid(row = 6, column = 1)
        self.bouton_jouer = tk.Button(self.root, text = "Jouer", command = self.jouer, fg = 'white', bg = "#FF00E6")
        self.bouton_jouer.grid(row = 6, column = 2)
        
        # Initialisation jeu
        x1 = rd.randint(0, 900)
        y1 = rd.randint(0, 500)
        x2 = rd.randint(0, 900)
        y2 = rd.randint(0, 500)
        vx = -10
        vy = 0
        self.score = 0
        self.carré = Carré.Carré(self.canvas, x1, y1, vx, vy, 50, 50, "#FFFFFF")
        self.pomme = Pomme.Pomme(self.canvas, x2, y2, 25, "#FF0000")
        self.carré = []
        self.creer_carré()

        # Boucle principale lancée si le bouton jouer est cliqué
        if self.bouton_jouer == True :
                self.jouer()
        self.root.mainloop()

    def creer_carré(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Crée le carré avec sa vitesse
            et les ajoute à self.carré.
        """
        x1, y1 = self.carré.coords()
        vx, vy = self.carré.vitesse()
        carré = Carré(self.canvas, x1 + 1, y1, vx, vy, 50, 50, 'purple')
        self.carré.append(carré)

    
    def verifier_collision_bords(self, obj):
        """
        Entrée :
            obj : instance ayant une méthode coords() renvoyant [x1,y1,x2,y2]
        Sortie :
            tuple(bool, str|None) : (True, 'x'|'y') si collision détectée et
            axe principal de pénétration, sinon (False, None).
        description de la fonction :
            Détecte la collision entre les carrés et le bord de la fenêtre
        """

        x1, y1 = obj.coords()               # coordonnées de l'objet (tête du serpent)
        if x1 <= 0 or x1 >= self.canvas.winfo_width():              
            return False
        if y1 <= 0 or y1 >= self.canvas.winfo_height():
            return False


    def jouer(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Boucle principale du jeu (appelée périodiquement). Déplace les carrés,
            gère les collisions avec les pommes et les bords, met à jour le
            score, gère les conditions de victoire/défaite et
            planifie l'appel suivant via self.root.after.
        """
        x1, y1 = self.carré.coords()    #on récupère les composantes nécéssaires
        vx, vy = self.carré.vitesse()
        
        self.carré.deplacer()
        collision = self.verifier_collision_bords(self.carré) # on vérifie s'il y a collision avec les bords
        if collision:
            self.message = self.canvas.create_text(450, 250, text = "Tu as perdu !", fill = "black", font = ("Helvetica", 30))
            return
        
        if self.score == 180 :
            self.message = self.canvas.create_text(450, 250, text = "Tu as gagné !", fill = "black", font = ("Helvetica", 30))
            return
        
    
        # Collision avec les pommes
        for pomme in self.pomme[:]:
            collision = self.verifier_collision(pomme)
            if collision:
                pomme.detruire()               #le canvas de la pomme se supprime après collision
                self.pomme.remove(pomme)     #on enlève la pomme mangée
                self.score += 1
                self.label_score.config(text=f"Score : {self.score}")
                carré = Carré(self.canvas, x1 + 1, y1, vy, vx, 50, 50, 'purple')
                self.carré.append(carré)

        self.root.after(10, self.jouer) #on relance la boucle

    
if __name__ == "__main__" :
    app = Snake()