""" TD 16

1. Créez une interface `Drawable` qui contient une méthode `draw`
2. Faites en sorte que `Carre` implémente cette interface.
3. Créez une classe `Triangle` qui hérite de `Shape` et implémente `Drawable`
4. Créer une méthode qui prend une `list` de `Drawable` et les dessiner toutes
"""
from TD14 import Shape, Point
from TD15 import Carre
import turtle as tt
import random


class Drawable:
    def draw(self):
        raise NotImplementedError


class Triangle(Shape, Drawable):
    def __init__(self,  color: str = "red", position: Point = Point(0, 0), length: int = 100):
        self.length = length
        # Nous avons un double héritage, attention au super ! Il vaut mieux préciser la classe
        # mais contrairement au super, il faut ajouter l'argument self
        Shape.__init__(self, color=color, position=position)

    def __move(self):
        tt.penup()
        tt.goto(self.position.x, self.position.y)
        tt.pendown()

    def __draw(self):
        tt.pencolor(self.color)
        for i in range(3):
            tt.forward(self.length)
            tt.left(120)

    def draw(self):
        self.__move()
        self.__draw()


def draw_all(list_drawable):
    for i in list_drawable:
        i.draw()


if __name__ == "__main__":
    l = [Carre(ra) for e in range(3)]
    []
    l.append(Carre())
    l.append(Triangle())
    l.append(Triangle(position=Point(10, 10), color="blue"))
    draw_all(l)
    tt.exitonclick()
