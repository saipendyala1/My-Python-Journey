import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (math.sqrt((self.x ** 2) + (self.y ** 2)))

    def distance_from_other_point(self, other_point):
        return (math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2))
    
    def slope(self, other_point):
        if not other_point.x - self.x == 0:
            return ((other_point.y - self.y)/(other_point.x - self.x))
        else:
            return 'inf'


class Polygon(Point):
    def __init__(self, points):
        self.points = points

    def get_perimeter(self):
        perimeter = 0
        for i in range(0, len(self.points)):
            if i == len(self.points)-1:
                perimeter += self.points[-1].distance_from_other_point(self.points[0])
            else:
                pt1 = self.points[i]
                pt2 = self.points[i+1]
                perimeter += pt1.distance_from_other_point(pt2)
        return perimeter


p1 = Point(0, 0)
p2 = Point(0, 5)
p3 = Point(5, 0)


print(p1.x, p1.y)
print(p1.distance_from_origin())
print(p2.distance_from_origin())

print()
print(p1.distance_from_other_point(p2))
print(p2.distance_from_other_point(p1))
print(p2.distance_from_other_point(p2))

print()
print(p1.slope(p2))
print(p2.slope(p3))

print()
pg = Polygon([p1, p2, p3])
print(pg.get_perimeter())


