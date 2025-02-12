import time
import pygame

screenW=600
screenH=400
ground = 300

pygame.init()
screen = pygame.display.set_mode((screenW,screenH))
clock=pygame.time.Clock()
running=True
dt=0
num = 0
skierRect = pygame.transform.scale_by(pygame.image.load("to-ski-73994_640-removebg-preview.png"),.3)

##Photo by eberhard grossgasteiger: https://www.pexels.com/photo/snowy-mountain-1287145/


class Background:
        def __init__(self, char):
            self.position = 0
            self.char=char
            #as the background moves, position gets higher

        def getPosition(self):
            return self.position

        def setPosition(self, pos):
            self.position=pos

        def move(self, amount=1):
            self.position=self.position+amount
        
        def jump(self):
            self.char.jump()

class Skier:
    def __init__(self,positionP):
        self.xVelocity = 0
        self.yVelocity=0
        self.position=positionP

    def jump(self):
        print("jumpity jump")
        self.yVelocity = -50

       
    def getX (self):
        return self.position.x
    def getY(self):
        return self.position.y
    def getPosition(self):
        return self.position

    def calculateNextPos(self):
        self.position.y+=self.yVelocity
        self.position.x+=self.xVelocity
        if self.position.y<ground:
            self.yVelocity+=5
        if self.position.y>=ground:
            self.yVelocity = 0
            self.position.y=ground


def drawSkier(skier: Skier):
    # skierRect = pygame.Rect(skier.position, (200,200))
    # pygame.draw.ellipse(screen, "pink" ,skierRect)
    
    screen.blit(skierRect, (skier.position))

background = pygame.transform.scale_by(pygame.image.load("SKISKIYA.png"), .5)


def drawBackground(numb):
    screen.blit(background,(numb,-10))

def moveBackground(numb):
    if numb<=-1050:
        numb = 0
    else:
        numb-=10
    return numb

skiposvector = pygame.Vector2(100,-100);
skiingSonia = Skier(skiposvector)
grid = Background(skiingSonia)


while running:
    drawBackground(num)
    print(num)
    skiingSonia.calculateNextPos()
    drawSkier(skiingSonia)
    num = moveBackground(num)
    if skiingSonia.getY()>600:
        print(skiingSonia.getY())
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False;

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                grid.jump()
    time.sleep(.02)
    pygame.display.flip()
pygame.quit()