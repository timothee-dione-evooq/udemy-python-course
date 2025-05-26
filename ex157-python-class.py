class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def get_geometric_properties(self):
        area = self.area()
        perimeter = self.perimeter()
        print(f"Area: {area}\nPerimeter: {perimeter}")

rectangle = Rectangle(4,5)
rectangle.get_geometric_properties()