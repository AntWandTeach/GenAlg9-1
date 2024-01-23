import random
import pygame
import time
import sys
w = 750
h = 400
class animal():
  
    def otskok(self):
        if (self.x - 1 < 0) or (self.x+1>h):
            self.vx = -self.vx
        if (self.y - 1 < 0) or (self.y+1>w):
            self.vy = -self.vy
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def kushat(self, a):
        if a.x > self.x-5 and a.x < self.x+5 and a.y > self.y-5 and a.y < self.y+5: 
            a.hp += 100
            self.hp -= 100
    




class wolk(animal):
    def __init__(self,hp,x,y,vx,vy,tick):
        self.hp = hp
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.tick = tick
class zai(animal):
    def __init__(self,hp,x,y,vx,vy,tick):
        self.hp = hp
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.tick = tick


pygame.init()
screen = pygame.display.set_mode((w, h))

wolfs = [wolk(hp=100,x=random.randint(0,h),y=random.randint(0,w),vx=random.randint(1,5),vy=random.randint(1,5),tick=random.randint(100,300)) for i in range(25)]
zais = [zai(hp=100,x=random.randint(0,h),y=random.randint(0,w),vx=random.randint(1,5),vy=random.randint(1,5),tick=random.randint(100,300)) for i in range(50)]

def razmnojenie_zai(obj1,obj2):
    if obj1.x > obj2.x-5 and obj1.x < obj2.x+5 and obj1.y > obj2.y-5 and obj1.y < obj2.y+5 and obj1.tick > 500 and obj1.tick > 500:
        print("aaaaaaaaaaa")
        zais.append(zai(100,obj1.x,obj1.y,vx=random.randint(1,5),vy=random.randint(1,5),tick=1))
        obj1.tick = 400
        obj2.tick = 400
def razmnojenie_wolf(obj1,obj2):
    if obj1.x > obj2.x-5 and obj1.x < obj2.x+5 and obj1.y > obj2.y-5 and obj1.y < obj2.y+5 and obj1.tick > 500 and obj1.tick > 500:
        print("aaaaaaaaaaa")
        wolfs.append(wolk(100,obj1.x,obj1.y,vx=random.randint(1,5),vy=random.randint(1,5),tick=1))
        obj1.tick = 400
        obj2.tick = 400
iteration = 0
while True:
    iteration +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    #pygame.draw.rect(screen, (127, 127, 127), pygame.Rect(0, 0, w, h))
    kill=[]
    for i in range(len(zais)):
        if zais[i].hp < 1:
            kill.append(i)
    for i in range(len(kill)):
        zais.pop(kill[i]-i)

    
    kill=[]
    for i in range(len(wolfs)):
        if wolfs[i].hp < 1:
            kill.append(i)
    for i in range(len(kill)):
        wolfs.pop(kill[i]-i)
        
    for i in range(len(zais)):
        pygame.draw.circle(screen, (100,100,191),(zais[i].y, zais[i].x), 5)
        zais[i].move()
        zais[i].otskok()
        zais[i].tick += 1 
    for i in range(len(wolfs)):
        pygame.draw.circle(screen, (100,100,100),(wolfs[i].y, wolfs[i].x), 5)
        wolfs[i].move()
        wolfs[i].otskok()
        wolfs[i].tick += 1
        wolfs[i].hp -= 1
    
    for i in range(len(zais)):
        for g in range(len(wolfs)):
            zais[i].kushat(wolfs[g])
    for i in range(len(zais)):
        for g in range(len(zais)):
            if i!=g:
                razmnojenie_zai(zais[i],zais[g])
    for i in range(len(wolfs)):
        for g in range(len(wolfs)):
            if i!=g:
                razmnojenie_wolf(wolfs[i],wolfs[g])

            
    pygame.display.flip()
    
    print(iteration)
    time.sleep(0.1)
