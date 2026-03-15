import math
import random
import sys
import time

import networkx as nx

inf = float("inf")

print("task 0")

n = int(input())
graf = []
for i in range(n):
    x, y = map(float, input().split())
    graf.append((x, y))

visited = [False] * n
ma = [inf] * n
ma[0] = 0
ans = 0

for i in range(n):
    v = -1
    for j in range(n):
        if not visited[j] and (v == -1 or ma[j] < ma[v]):
            v = j

    visited[v] = True
    ans += ma[v]

    for to in range(n):
        if not visited[to]:
            d = math.sqrt((graf[v][0] - graf[to][0]) ** 2
                          + (graf[v][1] - graf[to][1]) ** 2)
            if d < ma[to]:
                ma[to] = d

print(ans)

print("task 1")

n = int(input())
words = input().split()
M, L = map(int, input().split())

graf = []
for i in range(M):
    row = input().split()
    graf.append(row)

shah = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

ans = set()


def dfs(x, y, word, idx, visited):
    if idx == len(word):
        return True

    if x < 0 or x >= M or y < 0 or y >= L:
        return False

    if visited[x][y]:
        return False

    if graf[x][y] != word[idx]:
        return False

    visited[x][y] = True

    for dx, dy in shah:
        nx, ny = x + dx, y + dy
        if dfs(nx, ny, word, idx + 1, visited):
            visited[x][y] = False
            return True

    visited[x][y] = False
    return False


for word in words:
    yes = False
    visited = [[False] * L for _ in range(M)]
    for i in range(M):
        for j in range(L):
            if dfs(i, j, word, 0, visited):
                ans.add(word)
                yes = True
                break
        if yes:
            break

print(' '.join(sorted(list(ans))))

print("task 2")


def prim(n, points):
    used = [False] * n
    min_edge = [inf] * n
    min_edge[0] = 0
    total_weight = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or min_edge[j] < min_edge[v]):
                v = j

        used[v] = True
        total_weight += min_edge[v]

        for to in range(n):
            if not used[to]:
                dist = math.sqrt((points[v][0] - points[to][0]) ** 2 +
                                 (points[v][1] - points[to][1]) ** 2)
                if dist < min_edge[to]:
                    min_edge[to] = dist

    return total_weight


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1
        return True


def kruskal(n, points):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2
                             + (points[i][1] - points[j][1]) ** 2)
            edges.append((dist, i, j))

    edges.sort()

    dsu = DSU(n)
    total_weight = 0
    edges_used = 0

    for dist, i, j in edges:
        if dsu.union(i, j):
            total_weight += dist
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_weight


def generate_points(n):
    points = []
    for i in range(n):
        x = random.uniform(-10000, 10000)
        y = random.uniform(-10000, 10000)
        points.append((x, y))
    return points


sizes = [10, 20, 50, 100, 200, 500, 800, 1000, 1500, 2000]

print("Размер | Прим (сек) | Краскал (сек)")
print("-" * 40)

for n in sizes:
    points = generate_points(n)

    start = time.time()
    prim_res = prim(n, points)
    prim_time = time.time() - start

    start = time.time()
    kruskal_res = kruskal(n, points)
    kruskal_time = time.time() - start

    if abs(prim_res - kruskal_res) > 1e-6:
        print(f"Ошибка: результаты не совпадают для n={n}")

    print(f"{n:5d} | {prim_time:8.4f} | {kruskal_time:8.4f}")

print("\nАлгоритмическая сложность:")
print("Прим (простая реализация): O(V^2)")
print("Краскал (с сортировкой): O(E log E)")
print("как можно заметить алгоритм прима в среднем быстрее Краскала")

print("task 3")

n, m = map(int, input().split())
ejs = []
for i in range(m):
    u, v, w = map(int, input().split())
    ejs.append((u - 1, v - 1, w))


def find(p, x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(p, rk, x, y):
    x = find(p, x)
    y = find(p, y)
    if x == y:
        return False
    if rk[x] < rk[y]:
        p[x] = y
    elif rk[x] > rk[y]:
        p[y] = x
    else:
        p[y] = x
        rk[x] += 1
    return True


for i in range(m):
    sejs = []
    for j in range(m):
        sejs.append((ejs[j][2], ejs[j][0], ejs[j][1], j))
    sejs.sort()

    p = list(range(n))
    rk = [0] * n

    ans = ejs[i][2]
    union(p, rk, ejs[i][0], ejs[i][1])
    ejs_used = 1

    for w, u, v, idx in sejs:
        if ejs_used == n - 1:
            break
        if union(p, rk, u, v):
            ans += w
            ejs_used += 1

    print(ans)

print("task 4")
inf = float("inf")
iput = list(map(int, input().split()))
n = iput[0]
m = iput[1]
centers = iput[2:]

g = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

d = [inf] * n

for c in centers:
    d[c] = 0

visited = [False] * n

for i in range(n):
    v = -1
    md = inf
    for j in range(n):
        if not visited[j] and d[j] < md:
            md = d[j]
            v = j

    if v == -1:
        break

    visited[v] = True

    for to, w in g[v]:
        if d[to] > d[v] + w:
            d[to] = d[v] + w

ans = 0
for i in range(n):
    if i not in centers and d[i] != inf:
        ans += d[i]

print(ans)

print("bonus 1")

p = []
rk = []
n = 0


def find1(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(x, y):
    xr = find1(x)
    yr = find1(y)
    if xr == yr:
        return False
    if rk[xr] < rk[yr]:
        p[xr] = yr
    elif rk[xr] > rk[yr]:
        p[yr] = xr
    else:
        p[yr] = xr
        rk[xr] += 1
    return True


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    com = line.split()
    cmd = com[0]

    if cmd == "RESET":
        n = int(com[1])
        p = list(range(n))
        rk = [0] * n
        print("RESET DONE")

    elif cmd == "JOIN":
        j, k = int(com[1]), int(com[2])
        if not union(j, k):
            print(f"ALREADY {j} {k}")

    elif cmd == "CHECK":
        j, k = int(com[1]), int(com[2])
        if find1(j) == find1(k):
            print("YES")
        else:
            print("NO")

print("bonus telegram 1")

G = nx.Graph()

ejs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
G.add_edges_from(ejs)

nve = G.number_of_nodes()
nejs = G.number_of_edges()
print(f"1) Число вершин: {nve}, число ребер: {nejs}")

components = list(nx.connected_components(G))

largest = max(components, key=len)

G_largest = G.subgraph(largest)

eccentricities = nx.eccentricity(G_largest)

radius = min(eccentricities.values())
diameter = max(eccentricities.values())
print(f"2) Радиус главной компоненты: {radius}, диаметр: {diameter}")

print("3) Кратчайшие пути:")
all_pairs = dict(nx.all_pairs_shortest_path_length(G))
for u in sorted(all_pairs.keys()):
    for v in sorted(all_pairs[u].keys()):
        if u < v:
            print(f"{u} -> {v}: {all_pairs[u][v]}")
