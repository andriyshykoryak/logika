#створи гру "Лабіринт"!
from typing import Any
from pygame import *
from pygame.sprite import *

from pygame.transform import scale, flip
from pygame.image import load
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = scale(load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 640:
            self.rect.y += self.speed
         
        if keys_pressed[K_RIGHT] and self.rect.x < 940:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed
        if self.rect.x <=700:
            self.direction = 'right'
        elif self.rect.x >= win_width - 80:
            self.direction = 'left'
class Wall(sprite.Sprite):
    def __init__(self, wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.image=Surface((self.width,self.height))
        self.image.fill((253,255,222))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image , (self.rect.x,self.rect.y))
    




win_width =1000
win_height = 700
clock = time.Clock()
FPS = 60

font.init()
ft = font.Font(None,70)
win = ft.render('You win',True,(252,45,1))
lose = ft.render('You lose',True,(0,255,0))

window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('m5\\maze\\background.jpg'),(win_width,win_height))

player = Player('m5\\maze\\hero.png',15,win_height-80,5)
cyborg = Enemy('m5\\maze\\cyborg.png',win_width-65,win_height-250,2)
final  = GameSprite('m5\\maze\\treasure.png',win_width-120,win_height-80,0)
wall1 = Wall(win_width-850,win_height-400,25,250)
wall2 = Wall(win_width-850,win_height-400,250,25)
wall3 = Wall(win_width-625,win_height-650,25,250)





walls = [wall1,wall2,wall3]



game = True
finish = False
mixer.init()
mixer.music.load('m5\\maze\\jungles.ogg')
mixer.music.play()
money=mixer.Sound('m5\\maze\\money.ogg')
kick = mixer.Sound('m5\\maze\\kick.ogg') 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        window.blit(background,(0,0))
        player.reset()
        cyborg.reset()
        final.reset()
        for w in walls:
            w.reset()
            if sprite.collide_rect(player,w):
                # finish = True
                kick.play()
                window.blit(lose,(500,350))
                player.rect.x -=20
                
                

        if sprite.collide_rect(player,final):
            finish = True
            window.blit(win,(500,350))
            money.play()
        if sprite.collide_rect(player,cyborg):
            finish = True
            window.blit(lose,(500,350))
            kick.play()
            
            


        player.update()
        cyborg.update()
    
    display.update()
    clock.tick(FPS)
