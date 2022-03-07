class Rectangle:

    def __init__(self, height, width):
        self.h = height
        self.w = width
    
    def perim(self):
        return (2 * self.h) + (2 * self.w)
    
    def area(self):
        return self.h * self.w
    
    def isSquare(self):
        #return (self.h == self.w)
        if self.h == self.w:
            return True
        else:
            return False
    
a1 = Rectangle(3,5)
print(a1.perim())
print(a1.area())
print(a1.isSquare())
print()

a2 = Rectangle(3,3)
perimeter = a2.perim()
print('perimeter: ', perimeter)
area = a2.area()
print('area: ', area)
print(a2.isSquare())