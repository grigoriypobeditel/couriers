class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def get_distance(self, point):
        vector_x = (point.x - self.x) ** 2
        vector_y = (point.y - self.y) ** 2
        return (vector_x + vector_y) ** 0.5


class Courier(Point):
    def __init__(self, x, y, name, weight, speed):
        super().__init__(x, y)
        self.name = name
        self.weight = weight
        self.speed = speed
        self.orders = []


class Order(Point):
    def __init__(self, x, y, name, weight):
        super().__init__(x, y)
        self.name = name
        self.weight = weight
        self.time = {
            "get_order": 0,
            "out_order": 0
        }

    def __repr__(self):
        return self.name
