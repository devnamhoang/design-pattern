from math import sqrt


class RoundPeg:
    radius: int

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def getRadius(self) -> int:
        return self.radius


class RoundHole:
    radius: int

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def getRadius(self) -> int:
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.radius >= peg.getRadius()


class SquarePeg:
    width: int

    def __init__(self, width: int) -> None:
        self.width = width

    def getWidth(self) -> int:
        return self.width


class SquarePegAdapter:
    peg: SquarePeg

    def __init__(self, peg: SquarePeg) -> None:
        self.peg = peg

    def getRadius(self) -> float:
        return self.peg.getWidth() * sqrt(2) / 2
