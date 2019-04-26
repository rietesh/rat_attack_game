import pygame
import random
import time

width = 800
height = 600
#delay = 20
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
fps = 30

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

functions = {
    'one' : rat,
    'two' : cheese,
    'three' : jerry
}
images = [
    (width*0.05,height*0.45),
    (width*0.25,height*0.45),
    (width*0.65,height*0.45),
    (width*0.45,height*0.45),
    (width*0.85,height*0.45)
]



delay = 1
while not quited:

    Display.fill((255,255,255))
    box(width*0.05,height*0.45)
    box(width*0.25,height*0.45)
    box(width*0.45,height*0.45)
    box(width*0.65,height*0.45)
    box(width*0.85,height*0.45)

    def create(dictionary,x,y):
        func = random.choice(list(dictionary))
        functionsss = functions[func]
        return functionsss(x,y);

    time.sleep(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quited = True

    tup = random.choice(images)
    create(functions,tup[0],tup[1])

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        (x,y) = pos
        print('----------')
        print(pos)
        print(tup)
        print('--------------')



    pygame.display.update()
    clock.tick(fps)
    delay += 2

pygame.quit()
quit()
