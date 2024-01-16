import pygame as pg

class zivotnie():
    def __init__(self,screen,x,y,ugol) -> None:
        self.tipe=""
        self.screen=screen
        self.image=pg.image.load("D:/vsc/урока/informatika/zaya.png")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.ugol=ugol
        self.coordx=float(x)
        self.coordy=float(y)
        self.hp=5
        self.kd=50
        

    def output(self):
        self.screen.blit(self.image,self.rect)