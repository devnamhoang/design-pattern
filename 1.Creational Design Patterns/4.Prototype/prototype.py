from abc import ABC, abstractmethod


class Shape(ABC):  # abstract class

    @abstractmethod
    def clone(self):
        pass


class Rectangle(Shape):

    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        # return self -> shallow copy (wrong)
        return Rectangle(self.x, self.y)  # --> deep copy (true)

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y)


class Circle(Shape):
    z: int

    def __init__(self, z):
        self.z = z

    def clone(self):
        # return self -> shallow copy (wrong)
        return Circle(self.z)  # --> deep copy (true)

    def __str__(self):
        return "z = " + str(self.z)


class Application:

    def __init__(self):
        rectangle = Rectangle(5, 10)
        other_rectangle = rectangle.clone()
        print(rectangle)
        print("address=", id(rectangle))
        print(other_rectangle)
        print("address=", id(other_rectangle))

        print()

        circle = Circle(5)
        other_circle = circle.clone()
        print(circle)
        print("address=", id(circle))
        print(other_circle)
        print("address=", id(other_circle))


run = Application()

# NOTE: MUST USE DEEP COPY AT LINE 20 and 33
