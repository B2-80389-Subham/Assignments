PI = 3.14


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return PI * self.r**2

    def perimeter(self):
        return 2 * PI * self.r


circleC = Circle(3, 4, 5)
area_of_circle = circleC.area()
perimeter_of_circle = circleC.perimeter()

print(f"Center: ({circleC.x}, {circleC.y})")
print(f"Radius: {circleC.r}")
print(f"Area: {area_of_circle:.2f}")
print(f"Perimeter: {perimeter_of_circle:.2f}")
