class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print(f"Height: {self.height}")
        print(f"Volume: {self.volume()}")


my_rectangle = Rectangle(5, 4)


print("Rectangle:")
my_rectangle.display()
print("\n")


my_parallelepiped = Parallelepiped(5, 4, 3)
print("Parallelepiped:")
my_parallelepiped.display()
