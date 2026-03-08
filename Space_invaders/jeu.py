from vaisseau import Vaisseau
from alien import Alien
from projectile import Projectile

class Jeu:
    def __init__(self, canvas, largeur=600, hauteur=400, nb_aliens_ligne=8, nb_aliens_col=3):
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.vaisseau = Vaisseau(canvas, largeur//2, hauteur - 30)
        self.projectiles = []
        self.aliens = []
        self.dx_alien = 5
        self.dy_alien = 20
        self.creer_aliens(nb_aliens_ligne, nb_aliens_col)
        self.aliens_direction = 1  # 1 = droite, -1 = gauche
        self.game_over = False
        self.win = False
        self.score = 0

    def creer_aliens(self, lignes, colonnes):
        espace = 10
        taille = 30
        for i in range(lignes):
            for j in range(colonnes):
                x = 50 + j*(taille + espace)
                y = 50 + i*(taille + espace)
                self.aliens.append(Alien(self.canvas, x, y, taille))

    def deplacer_vaisseau(self, dx):
        demi = self.vaisseau.largeur // 2
        if demi <= self.vaisseau.x + dx <= self.largeur - demi:
            self.vaisseau.deplacer(dx)

    def tirer(self):
        x = self.vaisseau.x
        y = self.vaisseau.y - self.vaisseau.hauteur//2
        self.projectiles.append(Projectile(self.canvas, x, y))

    def mise_a_jour(self):
        if not self.aliens:
            self.game_over = True
            self.win = True
            return

        # Déplacement aliens
        bord_droite = max(a.x + a.taille for a in self.aliens)
        bord_gauche = min(a.x for a in self.aliens)
        if bord_droite >= self.largeur or bord_gauche <= 0:
            self.aliens_direction *= -1
            for a in self.aliens:
                a.deplacer(0, self.dy_alien)
        else:
            for a in self.aliens:
                a.deplacer(self.dx_alien * self.aliens_direction)

        # Déplacement projectiles
        for p in self.projectiles:
            if p.active:
                p.deplacer(-10)

        # Collision projectiles / aliens
        for p in list(self.projectiles):
            if not p.active:
                continue
            for a in list(self.aliens):
                if (a.x < p.x < a.x + a.taille) and (a.y < p.y < a.y + a.taille):
                    self.canvas.delete(a.id)
                    self.aliens.remove(a)
                    p.active = False
                    self.canvas.delete(p.id)
                    self.score += 10
                    break

        # Nettoyage des projectiles inactifs
        self.projectiles = [p for p in self.projectiles if p.active]

        # Fin de jeu
        for a in self.aliens:
            if a.y + a.taille >= self.hauteur - 30:
                self.game_over = True