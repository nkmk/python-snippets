# https://docs.python.jp/3/library/collections.html#collections.namedtuple

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

print(Point)
# <class '__main__.Point'>

p1 = Point(1, 2)
print(p1)
print(type(p1))
# Point(x=1, y=2)
# <class '__main__.Point'>

print(p1.x, p1.y)
print(p1[0], p1[1])
# 1 2
# 1 2

p_new = p1._replace(x=10)
print(p1)
print(p_new)
# Point(x=1, y=2)
# Point(x=10, y=2)

p_d = p1._asdict()
print(p_d)
print(type(p_d))
# OrderedDict([('x', 1), ('y', 2)])
# <class 'collections.OrderedDict'>

print(Point._fields)
# ('x', 'y')

Point_3D = namedtuple('Point_3d', Point._fields + ('z', ))

print(Point_3D)
# <class '__main__.Point_3d'>

p_3d = Point_3D(1, 2, 3)
print(p_3d)
print(type(p_3d))
# Point_3d(x=1, y=2, z=3)
# <class '__main__.Point_3d'>

p2 = Point(3, 4)
print(p2)
# Point(x=3, y=4)

p = p1 + p2
print(p)
print(type(p))
# (1, 2, 3, 4)
# <class 'tuple'>

class Point_a(namedtuple('Point_a', ['x', 'y'])):
    def __add__(self, other):
        return Point_a(self.x + other.x, self.y + other.y)

p1_a = Point_a(1, 2)
p2_a = Point_a(3, 4)
print(p1_a)
print(p2_a)
# Point_a(x=1, y=2)
# Point_a(x=3, y=4)

p_a = p1_a + p2_a
print(p_a)
# Point_a(x=4, y=6)
