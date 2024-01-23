import pygame as pg
import sys,random,time
from zaya import Zaya
from wolf import Wolf

class Game():
    def __init__(self) -> None:        
        pg.init()
        screen=pg.display.set_mode((500,500))
        pg.display.set_caption("vizivanie")
        ZAYZI=[]
        WOLF=[]
        for i in range(20):
            zay=Zaya(screen,random.randint(0,490),random.randint(0,490),random.randint(0,360))
            ZAYZI.append(zay)
        for i in range(10):
            wolk=Wolf(screen,random.randint(0,490),random.randint(0,490),random.randint(0,360))
            WOLF.append(wolk)

        

        while(1):
            screen.fill((0,0,0))
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()

            for i in range(len(ZAYZI)):
                ZAYZI[i].move()
            for i in range(len(WOLF)):
                WOLF[i].move()

            kill=[]
            for i in range(len(WOLF)):
                for j in range(len(ZAYZI)):
                    if(WOLF[i].kd==50):
                        WOLF[i].kd=0
                        if(WOLF[i].rect.colliderect(ZAYZI[j])):
                            ZAYZI[j].hp_minus()
                            WOLF[i].tick_reburn()
                    else:
                        WOLF[i].kd+=5

            for i in range(len(ZAYZI)):
                if(ZAYZI[i].hp<=0):
                    kill.append(i)
            for i in range(len(kill)):
                ZAYZI.pop(kill[i]-i)

            kill=[]          
            for i in range(len(WOLF)):
                if(WOLF[i].tick_live<=0):
                    WOLF[i].hp-=1
                    WOLF[i].tick_reburn()
            for i in range(len(WOLF)):
                if(WOLF[i].hp<=0):
                    kill.append(i)
            for i in range(len(kill)):
                WOLF.pop(kill[i]-i)
            kill=0


            for i in range(len(ZAYZI)):
                for j in range(len(ZAYZI)):
                    if(ZAYZI[i].rect.colliderect(ZAYZI[j])):
                        if(ZAYZI[i].mojna_cex_vopros(ZAYZI[j])==True and i!=j):
                            ZAYZI[i].kd_cex_null()
                            ZAYZI[j].kd_cex_null()
                            ZAYZI.append(Zaya(screen,ZAYZI[i].rect.x,ZAYZI[i].rect.y,random.randint(0,360)))
                        else:
                            pass
            for i in range(len(WOLF)):
                for j in range(len(WOLF)):
                    if(WOLF[i].rect.colliderect(WOLF[j])):
                        if(WOLF[i].mojna_cex_vopros(WOLF[j])==True and i!=j):
                            WOLF[i].kd_cex_null()
                            WOLF[j].kd_cex_null()
                            WOLF.append(Wolf(screen,WOLF[i].rect.x,WOLF[i].rect.y,random.randint(0,360)))
                        else:
                            pass
        



            for i in range(len(ZAYZI)):    
                ZAYZI[i].kd_cex_increase()            
                ZAYZI[i].output()
            for i in range(len(WOLF)):
                WOLF[i].kd_cex_increase()
                WOLF[i].tick_little()
                WOLF[i].output()
            pg.display.flip()
            time.sleep(0.005)



a= Game()