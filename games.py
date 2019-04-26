import pygame
import random
import sys
from pygame.locals import *

width = 800
height = 600
pygame.init()
Display = pygame.display.set_mode((width,height))
pygame.display.set_caption('1st game')
clock = pygame.time.Clock()

quited = False
ratimg = pygame.image.load('rat.png')
ratimg = pygame.transform.scale(ratimg,(100,100))
boximg = pygame.image.load('box.png')
boximg = pygame.transform.scale(boximg,(150,150))
cheeseimg = pygame.image.load('cheese.png')
cheeseimg = pygame.transform.scale(cheeseimg,(100,100))
jerryimg = pygame.image.load('jerry.png')
jerryimg = pygame.transform.scale(jerryimg,(100,100))
fps = 60

def rat(x,y):
    Display.blit(ratimg,(x,y))

def box(x,y):
    Display.blit(boximg,(x*0.95,y*1.15))

def cheese(x,y):
    Display.blit(cheeseimg,(x,y))

def jerry(x,y):
    Display.blit(jerryimg,(x,y))

def scores(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("score: "+str(count),True,(0,0,0) )
    Display.blit(text,(0,0))

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                return (0,0)

functions = {
    'one' : rat,
    'two' : cheese,
    'three' : jerry
}
images = {
    'ondu' : (width*0.05,height*0.45),
    'eradu' : (width*0.25,height*0.45),
    'muru' : (width*0.45,height*0.45),
    'nalku' : (width*0.65,height*0.45),
    'idu' : (width*0.85,height*0.45)
}
verify = {
    '1' : [40,140],
    '2' : [200,300],
    '3' : [360,460],
    '4' : [520,620],
    '5' : [680,780]
}

def verification(loc1,a,func1):
    count = 0
    if loc1 == 'ondu' and verify['1'][0] <= a <= verify['1'][1]:
        if func1 == 'two':
            quit()
        else:
            count += 1
    else:
        pass
    if loc1 == 'eradu' and verify['2'][0] <= a <= verify['2'][1]:
        if func1 == 'two':
            quit()
        else:
            count += 1
    else:
        pass
    if loc1 == 'muru' and verify['3'][0] <= a <= verify['3'][1]:
        if func1 == 'two':
            quit()
        else:
            count += 1
    else:
        pass
    if loc1 == 'nalku' and verify['4'][0] <= a <= verify['4'][1]:
        if func1 == 'two':
            quit()
        else:
            count += 1
    else:
        pass
    if loc1 == 'idu' and verify['5'][0] <= a <= verify['5'][1]:
        if func1 == 'two':
            quit()
        else:
            count += 1
    else:
        pass
    return count

delay = 5
scr = 0
location = None
fun = None
while not quited:

    Display.fill((255,255,255))
    scores(scr)
    box(width*0.05,height*0.45)
    box(width*0.25,height*0.45)
    box(width*0.45,height*0.45)
    box(width*0.65,height*0.45)
    box(width*0.85,height*0.45)
    box(800,500)

    loc = random.choice(list(images))
    tup = images[loc]
    func = random.choice(list(functions))
    functionsss = functions[func]
    functionsss(tup[0],tup[1])

    pos = wait()
    print('{} == {}=={}'.format(location,pos[0],fun))
    ans = verification(location,pos[0],fun)
    scr += ans
    print(scr)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quited = True

    pygame.display.update()
    clock.tick(fps)

    print('another loop --------')
    location = loc
    fun = func

pygame.quit()
quit()
