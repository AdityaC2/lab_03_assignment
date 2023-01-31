class Shape:
    def __init__(self, length, width, radius, color):
        self.length = length
        self.width = width
        self.radius = radius
        self.color = color
class Square (Shape):
    def area(self):
        return self.length**2
class Rectangle (Shape):
    def area(self):
        return self.length*self.width
class Circle (Shape):
    def area(self):
        return 3.14*(self.r**2)
print('''Enter Shape:

[1] Square

[2] Rectangle

[3] Circle

''')

a = int(input())
if a == 1:
    x = int(input("\nEnter the length: "))
    c = input("\nEnter Color: ")
    obj = Square(x, 0, 0, c)
    print("\nThe Square is",obj.color,"colored.")
    print("\nThe Area of the Square is,", obj.area())
elif a == 2:
    x = int(input("\nEnter the length: "))
    c = input("\nEnter Color: ")
    obj = Rectangle(x, y, 0, c)
    print("\nThe Rectangle is",obj.color,"colored.")
    print("\nThe Area of the Rectangle is", obj.area())
elif a == 3:
    x = int(input("\nEnter the length: "))
    c = input("\nEnter Color: ")
    obj = Circle(0, 0, z, c)
    print("\nThe Circle is",obj.color,"colored.")
    print("\nThe Area of the Circle is", obj.area())
