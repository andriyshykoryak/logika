#Створи власний Шутер!
from typing import Any
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
lost = 0 
score =0 
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image = scale(load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_width
        self.height = player_height
    def reset(self):
        window.blit(self.image , (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()         
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - self.width:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
    def fire(self):
        pass
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0,win_width-100)
            lost=lost+1




win_width,win_height = 700,700
window = display.set_mode((win_width,win_height))
background = scale(image.load('m5\\shooter\\galaxy.jpg'),(win_width,win_height))
rocket = Player('m5\\shooter\\rocket.png',350,win_height-110,80,100,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,4))  
    monsters.add(enemy)

game = True


finish = False
FPS = 60
clock = time.Clock()
mixer.init()
mixer.music.load('m5\\shooter\\space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()
font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',36)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        text_lose = font1.render(f'Пропущенно:{lost}',True,(255,255,22))
        text_score = font2.render(f'Рахунок:{score}',True,(255,255,22))
        window.blit(text_lose,(5,50))
        window.blit(text_score,(5,10))
        rocket.reset()
        rocket.update()
        enemy.reset()
        monsters.draw(window)
        monsters.update()
        enemy.update()

    display.update()
    clock.tick(FPS)