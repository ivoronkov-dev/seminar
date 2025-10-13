import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self):
        self.type = "star"
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = "red"
        self.image = None


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self):
        self.type = "planet"
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = "green"
        self.image = None


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue

        dx = obj.x - body.x
        dy = obj.y - body.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance == 0:
            continue

        force = gravitational_constant * body.m * obj.m / (distance**2)

        force_x = force * dx / distance
        force_y = force * dy / distance
        
        body.Fx += force_x
        body.Fy += force_y


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    
    **dt** — шаг по времени
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.Vx += ax * dt
    body.Vy += ay * dt

    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список объектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


def calculate_angular_velocity(body, central_body):
    """Calculate the angular velocity of a body around a central body.
    
    Параметры:
    
    **body** — тело, для которого вычисляется угловая скорость.
    
    **central_body** — центральное тело, вокруг которого вращается body.
    """

    dx = body.x - central_body.x
    dy = body.y - central_body.y

    r = math.sqrt(dx**2 + dy**2)
    
    if r == 0:
        return 0

    vx = body.Vx - central_body.Vx
    vy = body.Vy - central_body.Vy

    cross_product = dx * vy - dy * vx
    v_tangent = abs(cross_product) / r

    angular_velocity = v_tangent / r if r != 0 else 0
    
    return angular_velocity


if __name__ == "__main__":
    print("This module is not for direct call!")