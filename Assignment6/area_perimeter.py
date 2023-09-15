import math


def circle_perimeter(radius):
    return 2 * math.pi * radius


def circle_area(radius):
    return math.pi * radius ** 2


def square_perimeter(side_length):
    return 4 * side_length


def square_area(side_length):
    return side_length ** 2


def rectangle_perimeter(length, width):
    return 2 * (length + width)


def rectangle_area(length, width):
    return length * width


while True:
    print("\nMenu:")
    print("1. Calculate the perimeter and area of a Circle")
    print("2. Calculate the perimeter and area of a Square")
    print("3. Calculate the perimeter and area of a Rectangle")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        perimeter = circle_perimeter(radius)
        area = circle_area(radius)
        print(f"Perimeter of the circle: {perimeter}")
        print(f"Area of the circle: {area}")
    elif choice == '2':
        side_length = float(input("Enter the side length of the square: "))
        perimeter = square_perimeter(side_length)
        area = square_area(side_length)
        print(f"Perimeter of the square: {perimeter}")
        print(f"Area of the square: {area}")
    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        perimeter = rectangle_perimeter(length, width)
        area = rectangle_area(length, width)
        print(f"Perimeter of the rectangle: {perimeter}")
        print(f"Area of the rectangle: {area}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
