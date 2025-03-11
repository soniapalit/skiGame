import time
import pygame
import expression_evaluator
import math

screenW=1050 
screenH=700 
ground = 550.0
terrainCounter = 0
terrainEnd = 81.38495


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
        #print("jumpity jump")
        self.yVelocity = -50

       
    def getX (self):
        return self.position.x
    def getY(self):
        return self.position.y
    def getPosition(self):
        return self.position

    def calculateNextPos(self):

        firstY = self.position.y
        self.position.y+=self.yVelocity
        self.position.x+=self.xVelocity
        if self.position.y<ground:
            self.yVelocity+=5
        if self.position.y>=ground:
            self.yVelocity = 0
            self.position.y=ground

        yNow = self.position.y
        if abs(firstY-yNow)>=10:
            print(f"counter:{terrainCounter}")

    

def drawSkier(skier: Skier):
    # skierRect = pygame.Rect(skier.position, (200,200))
    # pygame.draw.ellipse(screen, "pink" ,skierRect)
    
    screen.blit(skierRect, (skier.position))

background = pygame.transform.scale_by(pygame.image.load("SKISKIYA.png"), .8)

# get f as a file object
#f.readline().split(",")

def get_func(func, ho, vo, sv, sh):
    ho = expression_evaluator.get_value(ho)
    vo = expression_evaluator.get_value(vo)
    sv = expression_evaluator.get_value(sv)
    sh = expression_evaluator.get_value(sh)

    if func == "sin":
        def sinx(x):
            print(f"{sv} * math.sin({sh} * x + {ho}) + {vo}")
            return sv * math.sin(sh * x + ho) + vo
        return sinx
    elif func == "e":
        return lambda x : sv * math.exp(sh * x + ho) + vo
    

def getExpression (counter):
        typee = "sin"
        ho = "0.0"
        vo = "0.0"
        sv = "0.0"
        sh = "0.0"

        if counter <=6.28318530718:
            sv="1"
            sh="1"
            vo="pi/3"
            ho="3*pi/2"
        elif counter <=21.91422:
            sv="2"
            sh="0.5"
            vo="2*pi/3.07"
            ho="pi/2"
        elif counter <= 26.40571:
            sv="4"
            sh="0.5"
            vo="2*pi/3.07"
            ho="pi/2+.54"
        elif counter <= 31.69019:
            typee = "e"
            sv="1"
            sh="-1"
            vo="0.1"
            ho="26.8"
        elif counter <=81.38495:
            sv="3"
            sh="1/3"
            vo="3.1"
            ho="9"
        else:
            sv="1"
            sh="1/5"
            vo="5.1"
            ho="3*pi/2"


        equation = get_func(typee, ho, vo, sv, sh)
        print(equation)
        return equation(counter)
        

def drawBackground(numb):
    screen.blit(background,(numb,-20))

def moveBackground(numb):
    if numb<=-(1685):
        numb = 0
    else:
        numb-=10
    return numb

skiposvector = pygame.Vector2(100,-100)
skiingSonia = Skier(skiposvector)
grid = Background(skiingSonia)


while running:
    ground = 550 - 50 * getExpression (terrainCounter)
    drawBackground(num)
    terrainCounter+=.1
    if terrainCounter >= terrainEnd-1:
        terrainCounter=0
    
    #print (expression_evaluator.get_value("sin 1+3*pi/4+ pi/3"))
    #print(num)
    skiingSonia.calculateNextPos()
    drawSkier(skiingSonia)
    num = moveBackground(num)
    print(f'ypos: {skiingSonia.getY()}')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False;

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and skiingSonia.getY()==ground:
                grid.jump()
    time.sleep(.02)
    pygame.display.flip()
pygame.quit()