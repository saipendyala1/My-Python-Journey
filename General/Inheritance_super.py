# Inheritance is a concept in OOP in which a class derives (or inherits) 
# attributes and behaviors from another class without needing to implement them again.

""" class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


square = Square(4)
print(square.area())

rectangle = Rectangle(2,4)
print(rectangle.area())

# square is a special type of rectangle
# the above code does not reflect this point """


""" 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        # super is used to call init method 
        # of Rectangle class
        super().__init__(length, length)
    
square = Square(4)
print('Area: ', square.area())
print('Perimeter: ', square.perimeter()) """


""" 
# super() allows you to call methods of the superclass in your subclass.
# The primary function is to extend the functionality of the inherited method.
# super() saves you from needing to rewrite those methods in your subclass
# and allows you to swap out superclasses with minimal code changes.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        print(face_area)
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

cube = Cube(3)
print(cube.surface_area())

# .surface_area() and .volume() -  calculates area of a single face
# rather than reimplementing the area calculation, super() helps to extend area calculation.
# notice Cube class does not have init method
 """

# Python supports multiple inheritance
# subclass can inherit from multiple superclasses 
# that don’t necessarily inherit from each other (also known as sibling classes).


# build right pyramid (a pyramid with a square base) out of a Triangle and a Square:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

pyramid = RightPyramid(2, 4)
print(pyramid.area())


# method resolution order (MRO) - tells Python how to search inherited methods
# print(RightPyramid.__mro__) 






""" # build right pyramid (a pyramid with a square base) out of a Triangle and a Square:

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# Square, Triangle
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

pyramid = RightPyramid(2, 4)
print(pyramid.area())

# notice RightPyramid initializes partially with the .__init__() from the Square class.
# allows .area() to use the .length on the object, as is designed.

# method resolution order (MRO) - tells Python how to search inherited methods
print(RightPyramid.__mro__)
 """

# some points to remember
# ============
# separate classes with the same method name.
# causes issues with method resolution 
# When you’re using super() with multiple inheritance, it’s imperative to design 
# your classes to cooperate. 
