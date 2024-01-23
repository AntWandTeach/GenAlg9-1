import typing
from typing import List

FPS: int = 20
WIDTH: int = 640
HEIGHT: int = 480

MINPEACE: int = 5
MINENEMY: int = 5
MAXPEACE: int = 20
MAXENEMY: int = 20

COLORS: dict = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "GROUND": (60, 40, 25),
    "GRAY":(100, 100, 100)
}

class Animal:
    def __init__(self, coords: typing.List[int], hp: int = 10, speed: typing.List[int] = [5, 5]):
        self.hp: int = hp
        self.__coords: typing.List[int] = coords
        self.__speed: typing.List[int] = speed

    def getParams(self) -> dict:
        return {
            "hp": self.hp,
            "coords": self.__coords,
            "speed": self.__speed
        }
    
    def setSpeed(self, speed: typing.List[int]) -> typing.List[int]:
        self.__speed = speed
        return self.__speed
    
    def moveToX(self, x: int):
        if self.__coords[0] < x:
            self.__coords[0] += self.__speed[0]
        elif self.__coords[0] > x:
            self.__coords[0] -= self.__speed[0]
        
    def moveToY(self, y: int):
        if self.__coords[1] < y:
            self.__coords[1] += self.__speed[1]
        elif self.__coords[1] > y:
            self.__coords[1] -= self.__speed[1]
    

class Peaceful(Animal):
    def __init__(self, coords: List[int], radius: int, hp: int = 10, speed: List[int] = [5, 5]):
        super().__init__(coords, hp, speed)
        self.__radius = radius

    def getRadius(self) -> int:
        return self.__radius


class Victims(Animal):
    def __init__(self, coords: typing.List[int], hp: int = 10, speed: typing.List[int] = [5, 5], damage: int = 5):
        super().__init__(hp=hp, coords=coords, speed=speed)
        self.__damage = damage

    def attack(self, entities):
        for entity in entities:
            if isinstance(entity, Peaceful):
                if entity.getParams["coords"][0] == self.__coords[0] and entity.getParams["coords"][1] == self.getParams[1]:
                    entity.hp -= self.__damage
