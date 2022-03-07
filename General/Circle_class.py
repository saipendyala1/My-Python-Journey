class Circle():

    PI = 3.14
    
    def __init__(self, r):
        self.radius = r
    
    # PI * r**2
    def area(self):
        return(Circle.PI * self.radius**2)
    
    # perimeter (circumference - 2 * PI * r)
    def perimeter(self):
        return(2 * Circle.PI * self.radius)
    
    def diameter(self):
        return(2 * self.radius)


c1 = Circle(8)
print(c1.radius)

print(c1.area())
print(c1.perimeter())
