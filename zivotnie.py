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
        self.kd_cex=0

    def kd_cex_increase(self):
        self.kd_cex+=1
    
    def kd_cex_null(self):
        self.kd_cex=0
    def mojna_cex_vopros(self,other):
        if(self.kd_cex>=600 and other.kd_cex>=600):
            return True
        else:
            return False

    def output(self):
        self.screen.blit(self.image,self.rect)