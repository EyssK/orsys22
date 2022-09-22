"""
TD 14

1. Créez une classe `Point` qui comporte deux attributs : `x` et `y`.
2. Créez une classe `Shape` qui comporte un attribut `position` qui est un `Point` et `color` qui est une `str`
"""

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x:{self.x} y:{self.y}"


class Shape:
    def __init__(self, color: str, position: Point=Point(0, 0)):
        self.position: Point = position
        self.color: str = color


if __name__ == "__main__":
    p = Point(1, 3)
    s = Shape(1)
    print(s.position, s.color)
    s = Shape('red', p)
    print(s.position, s.color)
    s = Shape('red', 1)
    print(s.position, s.color)
