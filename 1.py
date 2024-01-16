import random
import pygame
import time
import sys
w = 1500
h = 800
class animal():
  
    def otskok(self):
        if (self.x - 1 < 0) or (self.x+1>h):
            self.vx = -self.vx
        if (self.y - 1 < 0) or (self.y+1>w):
            self.vy = -self.vy
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def kushat(self, obj):
        if obj.x == self.x and obj.y == self.y:
            obj.hp += 1
            self.hp -= 1
            


class wolk(animal):
    def __init__(self,hp,x,y,vx,vy):
        self.hp = hp
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
class zai(animal):
    def __init__(self,hp,x,y,vx,vy):
        self.hp = hp
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

pygame.init()
screen = pygame.display.set_mode((w, h))

wolfs = [wolk(hp=10,x=random.randint(0,h),y=random.randint(0,w),vx=random.randint(10,50),vy=random.randint(10,50)) for i in range(100)]
zais = [wolk(hp=10,x=random.randint(0,h),y=random.randint(0,w),vx=random.randint(10,50),vy=random.randint(10,50)) for i in range(100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    #pygame.draw.rect(screen, (127, 127, 127), pygame.Rect(0, 0, w, h))
    for i in range(len(wolfs)):
        pygame.draw.circle(screen, (100,100,100),(wolfs[i].y, wolfs[i].x), 5)
        pygame.draw.circle(screen, (100,100,191),(zais[i].y, zais[i].x), 5)
        wolfs[i].move()
        wolfs[i].otskok()
        zais[i].move()
        zais[i].otskok()
    for i in range(len(zais)):
        for g in range(len(wolfs)):
            zais[i].kushat(wolfs[g])
    pygame.display.flip()
    time.sleep(0.1)

