import sys
from collections import deque

# Спасибо за помощь DeepSeek

print("task 1")


def find_social_clusters(n=5, people=[[0, 1], [1, 0], [2, 3], [3, 4]]):
    graf = [[] for _ in range(n)]
    rgraf = [[] for _ in range(n)]
    for a, b in people:
        graf[a].append(b)
        rgraf[b].append(a)

    visited1 = [False] * n
    order = []

    def dfs1(v):
        visited1[v] = True
        for i in graf[v]:
            if not visited1[i]:
                dfs1(i)
        order.append(v)

    for i in range(n):
        if not visited1[i]:
            dfs1(i)

    visited2 = [False] * n
    ans = []

    def dfs2(v, you):
        visited2[v] = True
        you.append(v)
        for i in rgraf[v]:
            if not visited2[i]:
                dfs2(i, you)

    for v in reversed(order):
        if not visited2[v]:
            you = []
            dfs2(v, you)
            you.sort()
            ans.append(you)

    ans = [i for i in ans if len(i) > 1]
    ans.sort(key=lambda x: -len(x))
    return ans


# n = int(input())
# people = eval(input())
# print(find_social_clusters(n, people))

print(find_social_clusters())

print("task 2")


def igogo(n=5, from_here_x=3, from_here_y=3):
    sx = from_here_x - 1
    sy = from_here_y - 1

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    doska = [[-1] * n for _ in range(n)]
    doska[sx][sy] = 0

    queue = deque()
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()
        next_dist = doska[x][y] + 1
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and doska[nx][ny] == -1:
                doska[nx][ny] = next_dist
                queue.append((nx, ny))

    return doska


ans = igogo()

# n, x, y = map(int, input().split())
# ans = igogo(n, x, y)


for row in ans:
    print(*row)

print("task 3")

graf = {'A': {'B': 1, 'D': 1, 'C': 3},
        'B': {'A': 1, 'E': 5},
        'C': {'A': 3, 'D': 1},
        'D': {'A': 1, 'C': 1, 'E': 3, 'F': 9},
        'E': {'B': 5, 'D': 3, 'G': 7},
        'G': {'E': 7, 'F': 8},
        'F': {'D': 9, 'G': 8}
        }


def all_vertex(graf):
    return list(graf.keys())


print(all_vertex(graf))


def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())


print(vertex_neighbors(graf, 'D'))


def value(graf, vertex1, vertex2):
    return (graf[vertex1][vertex2])


print(value(graf, 'A', 'D'))


def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex is None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = (shortest_path[current_min_vertex] +
                               value(graf, current_min_vertex, neighbor))
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path


def print_result(previous_vertex, shortest_path,
                 start_vertex, target_vertex):
    path = []
    vertex = target_vertex
    while vertex != start_vertex:
        path.append(vertex)
        vertex = previous_vertex[vertex]
    path.append(start_vertex)
    print("->".join(reversed(path)))
    print(shortest_path[target_vertex])


previous_vertex, shortest_path = dijkstra(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')


def dijkstra1(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    not_today = float('inf')
    for v in unvisited_vertexes:
        shortest_path[v] = not_today
    shortest_path[start] = 0

    while unvisited_vertexes:
        current = None
        for v in unvisited_vertexes:
            if current is None or shortest_path[v] < shortest_path[current]:
                current = v

        for nb in vertex_neighbors(graf, current):
            new_cost = max(shortest_path[current], value(graf, current, nb))
            if new_cost < shortest_path[nb]:
                shortest_path[nb] = new_cost
                previous_vertex[nb] = current

        unvisited_vertexes.remove(current)

    return previous_vertex, shortest_path


def dijkstra2(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    not_today = float('inf')
    for v in unvisited_vertexes:
        shortest_path[v] = not_today
    shortest_path[start] = 1

    while unvisited_vertexes:
        current = None
        for v in unvisited_vertexes:
            if current is None or shortest_path[v] < shortest_path[current]:
                current = v

        for nb in vertex_neighbors(graf, current):
            new_cost = shortest_path[current] * value(graf, current, nb)
            if new_cost < shortest_path[nb]:
                shortest_path[nb] = new_cost
                previous_vertex[nb] = current

        unvisited_vertexes.remove(current)

    return previous_vertex, shortest_path


def to_int(s):
    return 0 if s == "" else int(s)


def dijkstra3(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    for v in unvisited_vertexes:
        shortest_path[v] = None
    shortest_path[start] = ""

    while unvisited_vertexes:
        current = None
        for v in unvisited_vertexes:
            if shortest_path[v] is None:
                continue
            if (current is None or to_int(shortest_path[v]) <
                    to_int(shortest_path[current])):
                current = v

        if current is None:
            break

        for nb in vertex_neighbors(graf, current):
            new_str = shortest_path[current] + str(value(graf, current, nb))
            if (shortest_path[nb] is None or
                    to_int(new_str) < to_int(shortest_path[nb])):
                shortest_path[nb] = new_str
                previous_vertex[nb] = current

        unvisited_vertexes.remove(current)

    return previous_vertex, shortest_path


def dijkstra4(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    for v in unvisited_vertexes:
        shortest_path[v] = -float('inf')
    shortest_path[start] = float('inf')

    while unvisited_vertexes:
        current = None
        for v in unvisited_vertexes:
            if current is None or shortest_path[v] > shortest_path[current]:
                current = v

        for nb in vertex_neighbors(graf, current):
            new_cost = min(shortest_path[current], value(graf, current, nb))
            if new_cost > shortest_path[nb]:
                shortest_path[nb] = new_cost
                previous_vertex[nb] = current

        unvisited_vertexes.remove(current)

    return previous_vertex, shortest_path


def dijkstra5(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    not_today = (float('inf'), float('inf'))
    for v in unvisited_vertexes:
        shortest_path[v] = not_today
    shortest_path[start] = (0, 0)

    while unvisited_vertexes:
        current = None
        for v in unvisited_vertexes:
            if current is None or shortest_path[v] < shortest_path[current]:
                current = v

        cur_changes, cur_len = shortest_path[current]
        for nb in vertex_neighbors(graf, current):
            change = 1 if colours[current] != colours[nb] else 0
            new_changes = cur_changes + change
            new_len = cur_len + value(graf, current, nb)
            new_cost = (new_changes, new_len)

            if new_cost < shortest_path[nb]:
                shortest_path[nb] = new_cost
                previous_vertex[nb] = current

        unvisited_vertexes.remove(current)

    return previous_vertex, shortest_path


previous_vertex, shortest_path = dijkstra1(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')

previous_vertex, shortest_path = dijkstra2(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')

previous_vertex, shortest_path = dijkstra3(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')

previous_vertex, shortest_path = dijkstra4(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')

colours = {
    'A': 'red', 'B': 'blue', 'C': 'red', 'D': 'green',
    'E': 'blue', 'F': 'green', 'G': 'red'
}

previous_vertex, shortest_path = dijkstra5(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')
