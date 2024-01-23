from data import Animal, Victims, Peaceful
from data import WIDTH, HEIGHT, COLORS, FPS
from data import MAXENEMY, MAXPEACE, MINENEMY, MINPEACE
import pygame as pg
import random as r
from time import sleep
import typing
import sys

pg.init()
clock = pg.time.Clock()
pg.display.set_caption("Роблокс (не китайский)")
screen = pg.display.set_mode((WIDTH, HEIGHT))

entities: typing.List[typing.Union[Animal, Victims, Peaceful]] = []

def drawAnimalAt(obj: typing.Union[Animal, Victims, Peaceful], coords: typing.List[int], surface: pg.Surface = screen, 
                radius: int = 8, color: str = 'WHITE'):
    obj.moveToX(coords[0])
    obj.moveToY(coords[1])
    pg.draw.circle(surface, COLORS[color], obj.getParams()['coords'], radius)
    
def inRadius(x: typing.List[int], y: typing.List[int], radius: int) -> bool:
    if x[0] 

peaceful: typing.List[Peaceful] = []
victims: typing.List[Victims] = []
all: typing.List[typing.Union[Peaceful, Victims]] = []

for p in range(r.randint(MINPEACE, MAXPEACE)):
    pc: Peaceful = Peaceful([r.randint(0, WIDTH), r.randint(0, HEIGHT)])
    peaceful.append(pc)
    all.append(pc)

for v in range(r.randint(MINENEMY, MAXENEMY)):
    vc: Victims = Victims([r.randint(0, WIDTH), r.randint(0, HEIGHT)])
    victims.append(vc)
    all.append(vc)

print(all)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(COLORS['GROUND'])
    for item in all:
        if isinstance(item, Peaceful):
            drawAnimalAt(item, [r.randint(0, WIDTH), r.randint(0, HEIGHT)])
        else:
            drawAnimalAt(item, [r.randint(0, WIDTH), r.randint(0, HEIGHT)], color='GRAY')
    for peace in peaceful:
        for enemy in victims:
            pass
    pg.display.flip()
    clock.tick(FPS)
