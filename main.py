
class Circle:
    pi = 3.142
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return self.radius*self.pi

    def area(self):
        return self.pi*(self.radius**2)
circle1 = Circle(4)
print(f"the circumference of the circle is {circle1.circumference()}")
print(f"the area of the circle is {circle1.area()}")
