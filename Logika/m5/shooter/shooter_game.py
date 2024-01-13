#Створи власний Шутер!
from typing import Any
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer
lost = 0 
score =0 
finish = False
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
        global keys_pressed
        keys_pressed = key.get_pressed()         
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - self.width:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('m5\\shooter\\bullet.png',self.rect.centerx,self.rect.top,15,20,10)
        bullets.add(bullet)
        if keys_pressed[K_w]:
            self.fire()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0,win_width-100)
            lost=lost+1
 

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0,win_width-100)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0 :
            self.kill()


win_width,win_height = 700,700
window = display.set_mode((win_width,win_height))
background = scale(image.load('m5\\shooter\\galaxy.jpg'),(win_width,win_height))
rocket = Player('m5\\shooter\\rocket.png',350,win_height-110,80,100,5)
bullets = sprite.Group()

monsters = sprite.Group()
asteroids = sprite.Group()
for i in range(5):
    enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,4))  
    monsters.add(enemy)
for i in range(5):
    asteroid = Asteroid('m5\\shooter\\asteroid.png',randint(0,win_height),0,100,80,randint(1,4))
    asteroids.add(asteroid)
game = True


FPS = 60
clock = time.Clock()
mixer.init()
mixer.music.load('m5\\shooter\\space.ogg')
mixer.music.set_volume(1)
mixer.music.play()
font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',36)
font3 = font.SysFont('Arial',80)

ammo = 15
reload = False
round = 1
best_result = round
max_rounds = 4
while game:
   
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        if e.type == KEYDOWN:
            if e.key == K_UP:
                mixer_music.set_volume(1 + 0.25)
            if e.key == K_DOWN:
                mixer_music.set_volume(1 - 0.5)
            if e.key == K_RIGHT:
                mixer_music.set_volume(0)
            
        if e.type == KEYDOWN:
             
            if e.key == K_q:
                game = False
            if e.key == K_e:
                score = 10
            if e.key == K_w:
                for a in asteroids:
                    a.kill()
            if e.key == K_r:
                for i in range(5):
                    asteroid = Asteroid('m5\\shooter\\asteroid.png',randint(0,win_height),0,100,80,randint(1,4))
                    asteroids.add(asteroid)
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if ammo >= 0 and reload == False:
                    rocket.fire()
                    ammo -=1
            
                    if ammo == 0 and reload == False:
                        reload = True
                        start_reload = timer()

            
                
                

    if not finish:
        window.blit(background,(0,0))
        text_lose = font1.render(f'Пропущенно:{lost}',True,(255,255,22))
        text_score = font2.render(f'Рахунок:{score}',True,(255,255,22))
        ammo_amount = font2.render(f'Патрони:{ammo}',True,(255,255,22))
        round_txt = font2.render(f'Раунд: {best_result}',True,(255,255,22))
        best_result_txt = font2.render(f'Найкращий результат: {round}  раунди',True,(255,255,22))
        window.blit(text_lose,(5,50))
        window.blit(text_score,(5,10))
        window.blit(ammo_amount,(5,90))
        window.blit(round_txt,(5,130))
        window.blit(best_result_txt,(5,170))
        if reload == True:
            now_time = timer()
            delta = now_time - start_reload
            if delta < 3:
                ammo_text = font2.render(f'Патрони:   Зачекайте!Йде перезарядка',True,(255,255,22))
                window.blit(ammo_text,(5,90))
            else:
                ammo = 15
                reload = False

        rocket.reset()
        
        rocket.update()
        asteroid.reset()
        monsters.draw(window)
        asteroids.draw(window)
        bullets.draw(window)
        asteroid.update()
        monsters.update()
        asteroids.update()
        bullets.update()
        if sprite.spritecollide(rocket,monsters,False):
            
            
            finish = True
            txt_lose_game = font3.render('You lose',True,(255,15,51))
            window.blit(txt_lose_game,(200,150))
          
            
        collide = sprite.groupcollide(monsters,bullets,True,True)
        for c in collide:
            score+=1
            enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,4))  
            monsters.add(enemy)



        if score == 10:
            
            txt_win_game = font3.render('You win',True,(24,156,155))
            window.blit(txt_win_game,(250,500))
            time.delay(2000)
            score = 0
            round +=1
            if round == 2:
                ammo = 25
                for i in range(7):
                    enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,3))  
                    monsters.add(enemy)
                if score == 15:
                    
                    time.delay(2000)
                    txt_win_round_2 = font3.render('You win the second round',True,(24,156,155))
                    window.blit(txt_win_round_2,(250,500))
                    score = 0
                    round +=1
            if round == 3:
                ammo = 30
                for i in range(12):
                    enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,2))  
                    monsters.add(enemy)
                if round == 3 and score >= 20:
                    finish = True
                    txt_win_game = font3.render('You win', True, (24, 156, 155))
                    window.blit(txt_win_game, (250, 500))
                    round+=1
            if round == 4:
                ammo = 40
                for i in range(15):
                    enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,2))  
                    monsters.add(enemy)
                if score == 35:
                    round +=1
            if max_rounds == round:
                finish = True
                txt_win_game = font3.render('You win', True, (24, 156, 155))
                window.blit(txt_win_game, (250, 500))


    else:
        if finish == True:
            ammo=15
            finish = False
            score = 0
            lost = 0


        for m in monsters:
            m.kill()
        for a in asteroids:
            a.kill()
        for b in bullets:
            b.kill()
        for i in range(5):
            enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,4))  
            monsters.add(enemy)
 

        
        
        time.delay(3000)  

        


    display.update()
    clock.tick(FPS)
    
