from pygame import *

window = display.set_mode((700,500))

display.set_caption('Доганялки')
img = image.load('m5\\u1\\background.png')
clock = time.Clock()
FPS = 60
SPEED = 10


background = transform.scale(img,(700,500))
sprite1 = transform.scale(image.load('m5\\u1\\sprite1.png'),(100,100))
x1 = 200
y1 = 300

sprite2 = transform.scale(image.load('m5\\u1\\sprite2.png'),(100,100))
x2 = 400
y2 = 400


is_runnig = True

while is_runnig:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))



    for e in event.get() :
        if e.type == QUIT:
            is_runnig = False
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1>5:
        x1 -= SPEED
    if key_pressed[K_RIGHT] and x1<600:
        x1 += SPEED
    if key_pressed[K_UP] and y1 >0:
        y1 -= SPEED
    if key_pressed[K_DOWN] and y1<405:
        y1 += SPEED
    if key_pressed[K_a] and x2>5:
        x2 -= SPEED
    if key_pressed[K_d] and x2<600:
        x2 += SPEED
    if key_pressed[K_w] and y2 >0:
        y2 -= SPEED
    if key_pressed[K_s] and y2<405:
        y2 += SPEED

    


    








    display.update()
    clock.tick(FPS)
