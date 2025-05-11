from pygame import*
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QGroupBox, QRadioButton , QButtonGroup


class GameSprite(sprite.Sprite):
    def __init__(self, image_, x, y, speed ,w ,h):
        super().__init__()
        self.image = transform.scale(image.load(image_),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

class Player1 (GameSprite):
    def move(self, keys):
        if keys[K_UP]:
            self.rect.y -= 5
        elif keys[K_DOWN]:
            self.rect.y += 5
    def update(self):
        if self.rect.y > 480:
            self.rect.y = 50

class Player2 (GameSprite):
    def move(self, keys):
        if keys[K_RIGHT]:
            self.rect.y -= 5
        elif keys[K_LEFT]:
            self.rect.y += 5
    def update(self):
        if self.rect.y > 480:
            self.rect.y = 470

class Cyborg (GameSprite):
    def __init__(self, image_, x, y, speed ,w ,h,speedx,speedy):
        super().__init__(image_, x, y, speed ,w ,h)
        self.speedx=speedx
        self.speedy=speedy

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y < 0:
            self.rect.y = 0
            self.speedy = -self.speedy
        if self.rect.y > 430:
            self.rect.y = 430
            self.speedy = +self.speedy
        if self.rect.x > 650:
            self.rect.x = 650
            self.speedx = -self.speedx
        if self.rect.x <0:
            self.rect.x = 0
            self.speedx = +self.speedx
        







window = display.set_mode((700,500))
display.set_caption('Шутер')
background = transform.scale(image.load('платформа.png'),(700,500))
clock = time.Clock()

player1 = Player1('hero.png', 5,5,5,65,65)
player2 = Player2('hero.png', 630,5,5,65,65)
cyborg = Cyborg('cyborg.png',300,410,2,65,65,1,-2)









game = True
scene  = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys = key.get_pressed()
    player1.move(keys)
    player2.move(keys)
    cyborg.update()
    if keys[K_SPACE] and last_reload < 0:
        last_reload = reload
        x = player.rect.x + 29
        y = player.rect.y
    if player1.rect.colliderect(cyborg.rect):
        cyborg.rect.x -= cyborg.speed
    
    window.blit(background, (0,0))
    player1.reset()
    player2.reset()
    cyborg.reset()



    display.update()


