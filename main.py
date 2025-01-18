import time
import pygame

screenW=600
screenH=400

pygame.init();
screen = pygame.display.set_mode((screenW,screenH));
clock=pygame.time.Clock()
running=True;
dt=0;


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
        
        self.position=positionP
        self.x = self.position.x
        self.y=self.position.y
    def jump(self):
        print("jumpity jump")
        for i in range(0,10):
            time.sleep(1)
            self.y=self.y+1
        for i in range(0,10):
            time.sleep(1)
            self.y=self.y-1
    def getX (self):
        return self.x
    def getY(self):
        return self.y
    def getPosition(self):
        return self.position

skiposvector = pygame.Vector2(0,600);
mySkier = Skier(skiposvector)
grid = Background(mySkier)

while running:
    if mySkier.getY()>600:
        print(mySkier.getY())
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False;

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                grid.jump()
                print("jump")

pygame.quit()