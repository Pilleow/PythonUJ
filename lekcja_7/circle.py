import math

from points import Point


class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return self.radius * self.radius * math.pi

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        center_dist = ((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2) ** 0.5

        if center_dist + min(self.radius, other.radius) <= max(self.radius, other.radius):
            return self if self.radius >= other.radius else other # tutaj jeden okrąg zawiera się w drugim

        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        if center_dist == 0:
            new_center = self.pt
        else:
            factor = (center_dist + other.radius - self.radius) / (2 * center_dist)
            new_center_x = self.pt.x + dx * factor
            new_center_y = self.pt.y + dy * factor
            new_center = Point(new_center_x, new_center_y)
        new_radius = (center_dist + self.radius + other.radius) / 2
        return Circle(new_center.x, new_center.y, new_radius)

