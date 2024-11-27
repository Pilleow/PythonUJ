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
            return self if self.radius >= other.radius else other

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

    @classmethod
    def from_points(cls, points):
        # https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates

        if len(points) != 3:
            raise ValueError("podaj dokładnie trzy punkty")
        p1, p2, p3 = points

        d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
        if d == 0:
            raise ValueError("punkty nie tworzą okręgu")

        ux = (
                     (p1.x ** 2 + p1.y ** 2) * (p2.y - p3.y) +
                     (p2.x ** 2 + p2.y ** 2) * (p3.y - p1.y) +
                     (p3.x ** 2 + p3.y ** 2) * (p1.y - p2.y)
             ) / d
        uy = (
                     (p1.x ** 2 + p1.y ** 2) * (p3.x - p2.x) +
                     (p2.x ** 2 + p2.y ** 2) * (p1.x - p3.x) +
                     (p3.x ** 2 + p3.y ** 2) * (p2.x - p1.x)
             ) / d

        radius = math.sqrt((ux - p1.x) ** 2 + (uy - p1.y) ** 2)
        return cls(ux, uy, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius


    @property
    def width(self):
        return 2 * self.radius


    @property
    def height(self):
        return 2 * self.radius


    @property
    def topleft(self):
        return Point(self.left, self.top)


    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)


    @property
    def topright(self):
        return Point(self.right, self.top)


    @property
    def bottomright(self):
        return Point(self.right, self.bottom)


if __name__ == "__main__":
    c = Circle.from_points([Point(1.815287, 3.1525), Point(-0.5511, 2.14251), Point(5.687351, -3.51985532)])
    print(c.radius, c.pt)
