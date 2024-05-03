class Rotation:
        rotate = float
class Counter:
        count = int

class Shape:
    def __init__(self):
        pass
    def draw(self)->None:
        pass
class Circle(Shape, Counter):
    def __init__(self):
        super().__init__()

    def draw(self)->None:
        print("Drawing a circle")
class Square(Shape, Rotation):
    def __init__(self):
        super().__init__()

    def draw(self)->None:
        print("Drawing a square")
class Rectangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self)->None:
        print("Drawing a rectangle")
class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self)->None:
        print("Drawing a triangle")

class ShapeFactory:
    def __init__(self): pass
    def createShape(self)->Shape: pass

class CircleFactory(ShapeFactory):
    def __init__(self):
        super().__init__()
        self.circle = Circle()

    def createShape(self)->Shape:
        self.countCircle()
        return self.circle

    def countCircle(self):
        self.circle.count += 1

    def count(self)->int:
        return self.circle.count

class SquareFactory(ShapeFactory):
    def __init__(self):
        super().__init__()
        self.squre = Square()

    def createShape(self)->Shape:
        return self.squre

    def setRotate(self, angle: float):
        self.squre.rotate = (angle + self.squre.rotate) % 360

    def rotate(self) -> float:
        return self.squre.rotate

class RectangleFactory(ShapeFactory):
    def __init__(self):
        super().__init__()
        self.rectangle = Rectangle()

    def createShape(self)-> Shape:
        return self.rectangle


class TriangleFactory(ShapeFactory):
    def __init__(self):
        super().__init__()
        self.triangle = Triangle()
    def createShape(self)-> Shape:
        return self.triangle

class Drawing:
    def draw_shape(self, shape: ShapeFactory) -> None:
        shape.createShape().draw()


if __name__ == "__main__":
    drawing = Drawing()
    drawing.draw_shape(CircleFactory())
    drawing.draw_shape(SquareFactory())
    drawing.draw_shape(RectangleFactory())
    drawing.draw_shape(TriangleFactory())