import pygame as pg
from zivotnie import zivotnie
import math,random

class Zaya(zivotnie):
    def __init__(self, screen, x, y,ugol):
        super().__init__(screen, x, y,ugol)
        self.tipe="zaya"
        self.image=pg.image.load("D:/vsc/урока/informatika/zaya.png")
    
    def move(self):
        if(self.ugol==270):
                self.ugol=90
                self.coordy=499
        if(self.coordx<=0):
            if(self.ugol<180 and self.ugol>90):
                self.ugol=90-(self.ugol%90)
            elif(self.ugol>180 and self.ugol<270):
                self.ugol=360-(self.ugol%90)
            elif(self.ugol==180):
                 self.ugol=0+random.randint(-5,5)                 
        elif(self.coordx>=500):
            if(self.ugol<90 and self.ugol>0):
                self.ugol=180-(self.ugol%90)
            elif(self.ugol>270 and self.ugol<361):
                self.ugol=180+(90-self.ugol%90)
            elif(self.ugol==0):
                 self.ugol=0+random.randint(-5,5)       
        elif(self.coordy<=0):
            if(self.ugol>0 and self.ugol<90):
                self.ugol=360-(90-self.ugol%90)
            elif(self.ugol>90 and self.ugol<181):
                self.ugol=180+(90-self.ugol%90)
            elif(self.ugol==0):
                 self.ugol=0+random.randint(-5,5)
        elif(self.coordy>=500):
            if(self.ugol>=180 and self.ugol<271):
                self.ugol=90+self.ugol%90
            if(self.ugol>270 and self.ugol<361):
                self.ugol=90-self.ugol%90
        
        self.coordx=self.coordx+1*(math.sin(math.radians(90-self.ugol)))
        self.coordy=self.coordy-1*math.sin(math.radians(self.ugol))
        self.rect.x=int(self.coordx)
        self.rect.y=int(self.coordy)
    
    def hp_minus(self):
        self.hp-=1

    def output(self):
        return super().output()

