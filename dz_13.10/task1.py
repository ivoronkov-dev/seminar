print("task 1")

class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            self.decode(x)
        else:
            self.x = x
            self.y = y
            self.z = z

        assert all(isinstance(i, (int, float)) for i in (self.x, self.y, self.z)), \
            "Все координаты вектора должны быть числами"

    def decode(self, vector_str):
        parts = vector_str.strip('{} ').split(',')

        try:
            self.x = float(parts[0].strip())
            self.y = float(parts[1].strip())
            self.z = float(parts[2].strip())
        except ValueError:
            raise ValueError("у тебя буквы в координатах!")

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other

    def convert(self):
        return "{" + f"{self.x}, {self.y}, {self.z}" + "}"



def cmass(points):
    summa = Vector(0, 0, 0)
    for point in points:
        summa = summa + point

    c = summa *  (1/len(points))
    return c


def space(points):
    max_area = 0
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                a = points[i]
                b = points[j]
                c = points[k]
                ab = (b - a).__abs__()
                bc = (c - b).__abs__()
                ca = (a - c).__abs__()
                p = (ab + bc + ca)/2
                area = p*(p-ab)*(p-bc)*(p-ca)


                if area > max_area:
                    max_area = area

    return max_area**0.5





v1 = Vector(4, 2, 3)
v2 = Vector("{4, 5, 6}")
print(f"v1 * v2 (скалярное) = {v1 * v2}")

points = [
        Vector(0, 0, 0),
        Vector(4, 0, 0),
        Vector(0, 6, 0),
        Vector(1, 1, 2),
        Vector(5, 2, 1),
        Vector(2, 5, 0),
        Vector(0, 0, 4)
    ]
print(f"Центр масс: {cmass(points).convert()}")
print(f"Максимальная площадь: {space(points)}")







