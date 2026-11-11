class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0
    def describe(self):
        print("This is a", self.name)
class Rectangle(Shape):
    def __init__(self, length, width):
         super().__init__("Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def describe(self):
        super().describe()
        print("Radius =", self.radius)
class Calculator:
    def add(self, *args):
        return sum(args)
r = Rectangle(5, 4)
c = Circle(3)

calc = Calculator()
print("Sum with 1 arg =", calc.add(10))
print("Sum with 2 args =", calc.add(10, 20))
print("Sum with 3 args =", calc.add(10, 20, 30))
