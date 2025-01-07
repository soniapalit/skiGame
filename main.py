import time;
import pygame;
screenW=600
screenH=400

pygame.init();
screen = pygame.display.set_mode((screenW,screenH));
clock=pygame.time.Clock()
running=True;
dt=0;


#stuff



class skier:
    def __init__(self,position):
        self.x = 0;
        self.y=0;
        self.position=position


    def getX (self):
        return self.x
    def getY(self):
        return self.y




pygame.quit()