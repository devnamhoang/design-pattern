from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):  # INTERFACE

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass


class Dot(Graphic):  # implement interface
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        pass


class CompundGraphic(Graphic):

    children: List[Graphic]  # type: ignore

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.pop(child)

    def move(self, x, y):
        for item in self.children:
            item.move(x, y)

    def draw(self):
        # implement drawing
        pass


class Circle(Dot):
    radius: int
    
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y)
        self.radius = radius
        
    def draw(self):
        # draw
        pass


class ImageEditor:
    compound: CompundGraphic
    
    def __init__(self) -> None:
        pass
    
    def load(self):
        self.compound = CompundGraphic()
        self.compound.add(Dot(1, 2))
        self.compound.add(Circle(3, 5, 7))
        # ...