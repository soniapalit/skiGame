import time
import pygame
import expression_evaluator
import math

screenW=1050 
screenH=700 
ground = 550.0
terrainCounter = 1
terrainEnd = 81.38495
counterSpeedMultiplier = 35

#placing spikes on ground 🌵
#HIT DETECTION 🎯


pygame.init()
screen = pygame.display.set_mode((screenW,screenH))
clock=pygame.time.Clock()
running=True
dt=0
num = 0
numFore = 1000 #(terrainCounter*700)/81
skierRect = pygame.transform.scale_by(pygame.image.load("to-ski-73994_640-removebg-preview.png"),.3)

##Photo by eberhard grossgasteiger: https://www.pexels.com/photo/snowy-mountain-1287145/



class obstacle:
    def __init__(self,x):
        self.x=x
        self.inView=False

    def getInView(self,counter):
        if self.x>counter and self.x<(counter+(screenW/35)):
            #TODO make sure u take into account that there are two foregrounds not just one
            return True
        else:
            return False
    

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
            self.yVelocity+=1
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
foreground = pygame.transform.scale_by(pygame.image.load("SNOWYHILSSDESMOS.png"), 4)
#https://www.deviantart.com/ladylockedinthetower/art/Cactus-253452385
cutiecactus = pygame.transform.scale_by(pygame.image.load("cactuscuteobstacle.png"),0.1)

# get f as a file object
#f.readline().split(",")

def get_func(func, ho, vo, sv, sh):
    ho = expression_evaluator.get_value(ho)
    vo = expression_evaluator.get_value(vo)
    sv = expression_evaluator.get_value(sv)
    sh = expression_evaluator.get_value(sh)

    if func == "sin":
        def sinx(x):
            # print(f"{sv} * math.sin({sh} * x + {ho}) + {vo}")
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
            vo="2*pi/3.07+-2"
            ho="pi/2+0.54"
        elif counter <= 31.69019:
            typee = "e"
            sv="1"
            sh="-1"
            vo="0.1"
            ho="26.8"
        elif counter <=62.832:
            sv="5"
            sh="1/5"
            vo="5.1"
            ho="3*pi/2"
        else:
            sv="3"
            sh="1/3"
            vo="3.1"
            ho="9"


        equation = get_func(typee, ho, vo, sv, sh)
        
        # print(f"f({counter}) = {equation(counter)}")
        return equation(counter)
        

def drawForeground(numb2):
    print ("numb2:", numb2)
    screen.blit(foreground,(numb2,-450))
    if numb2 < -1800:
        screen.blit(foreground,(2800+numb2,-450))
def drawBackground(numb):
    screen.blit(background,(numb,-20))

def moveBackground(numb):
    if numb<=-(1685):
        numb = 0
    else:
        numb-=10
    return numb

def moveForeground(numb2):
    # if numb2 <= -70000:
    #     numb2=0
    # else:
    #     
    numb2=-(terrainCounter*counterSpeedMultiplier) + 155
    return numb2

skiposvector = pygame.Vector2(100,-100)
skiingSonia = Skier(skiposvector)
grid = Background(skiingSonia)
obstacles = []
spikes = obstacle(30)
obstacles.append(spikes)
obstacles.append(obstacle(50))

obstacles.append(obstacle(75))


while running:
    ground = 550 - 50 * getExpression (terrainCounter)
    print(f"Ground = {ground}")
    print(f"cpunter: {terrainCounter}")
    drawBackground(num)
    drawForeground(numFore)
    if True: #spikes.getInView(terrainCounter):
        for kiki in obstacles:
            spike_ground = 550 - 50 * getExpression (kiki.x)
            screen.blit(cutiecactus,((kiki.x - terrainCounter)*counterSpeedMultiplier,spike_ground+50))

    terrainCounter+=.1 * 2
    if terrainCounter >= terrainEnd:
        terrainCounter=0
    
    #print (expression_evaluator.get_value("sin 1+3*pi/4+ pi/3"))
    #print(num)
    skiingSonia.calculateNextPos()
    drawSkier(skiingSonia)
    num = moveBackground(num)
    numFore = moveForeground(numFore)
    # print(f'ypos: {skiingSonia.getY()}')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False;

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and skiingSonia.getY()>=ground-10:
                grid.jump()
    time.sleep(.01)
    pygame.display.flip()
pygame.quit()