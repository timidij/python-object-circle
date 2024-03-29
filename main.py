class Circle():
    pi = 3.142
    def __init__ (self, radius):
        self.radius = radius

    def circumference(self):
        return self.radius * self.pi
cool = Circle( 4 )
print(cool.circumference())