import random
import pygame
w = 1920
h = 1080
class animal():
  
    def otskok(x,y):
        if (x - 1 < 0) and (x+1>w):
            vx = -vx
        if (y - 1 < 0) and (y+1>w):
            vy = -vy
    


class wolk(animal):
    def __init__(self,hp,x,y,vx,vy):
        self.hp = hp
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
pygame.init()
screen = pygame.display.set_mode((w, h))

wolfs = [wolk(hp=10,x=random.randint(0,h),y=random.randint(0,w),vx=1,vy=1) for i in range(100)]

while True:
    pygame.draw.rect(screen, (127, 127, 127), pygame.Rect(0, 0, w, h))
    pygame.draw.circle(screen, (255,225,255),(h, w), 50)

