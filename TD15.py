"""
TD 15

_ `turtle` est un module graphique qui permet de tracer des lignes. Les méthodes `forward`, `left`, `right`
permettent de tracer et tourner. `penup`et `pendown` de lever ou pas le stylo.
`setpos` permet de déplacer le curseur. _

1. Créez une classe `Carre` qui hérite de `Shape`.
2. Créez une méthode `draw` qui dessine le carré.
"""

import turtle as tt
from TD14 import Shape, Point


class Carre(Shape):
    def __init__(self,  color: str = "red", position: Point = Point(0, 0), length: int = 100):
        self.length = length
        super().__init__(color, position)

    def __get_position(self):
        return self.position.x, self.position.y

    def __move(self):
        tt.penup()
        tt.goto(self.__get_position())
        tt.pendown()

    def __draw(self):
        tt.pencolor(self.color)
        for i in range(4):
            tt.forward(self.length)
            tt.left(90)

    def draw(self):
        self.__move()
        self.__draw()


if __name__ == "__main__":
    c = Carre(length=150)
    c.draw()
    c = Carre(position=Point(50,50), color="blue")
    c.draw()
    tt.exitonclick()
