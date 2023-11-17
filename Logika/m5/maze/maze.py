#створи гру "Лабіринт"!
from pygame import *

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







win_width =1000
win_height = 700
clock = time.Clock()
FPS = 60
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('m5\\maze\\background.jpg'),(win_width,win_height))

player = GameSprite('m5\\maze\\hero.png',15,win_height-80,5)
cyborg = GameSprite('m5\\maze\\cyborg.png',win_width-100,win_height-250,2)







game = True

mixer.init()
mixer.music.load('m5\\maze\\jungles.ogg')
mixer.music.play()

while game:
    window.blit(background,(0,0))
    player.reset()
    cyborg.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)
