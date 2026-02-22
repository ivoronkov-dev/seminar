print("task 1")

n, m, s, f = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append([b, w])
    g[b].append([a, w])

d = [float("inf")] * n
visited = [False] * n
parent = [-1] * n

d[s] = 0

for i in range(n):
    v = "bebebe"
    md = float("inf")
    for j in range(n):
        if not visited[j] and d[j] < md:
            md = d[j]
            v = j

    if v == "bebebe":
        break

    visited[v] = True

    for j in range(len(g[v])):
        to = g[v][j][0]
        w = g[v][j][1]
        if d[to] > d[v] + w:
            d[to] = d[v] + w
            parent[to] = v

ans = []
v = f
while v != -1:
    ans.append(v)
    v = parent[v]
ans.reverse()

print(len(ans))

print("task 2")

V, E = map(int, input().split())
vse_str = input().strip()

vse = []
vse_str = vse_str[2:-2]
mas = vse_str.split("}, {")
for i in range(V):
    if i < len(mas):
        if mas[i] == "":
            vse.append([])
        else:
            vse.append(list(map(int, mas[i].split(", "))))
    else:
        vse.append([])

visited = [False] * V
cycle = False


def dfs(v, bb):
    global cycle
    visited[v] = True
    for to in vse[v]:
        if not visited[to]:
            dfs(to, v)
        elif to != bb:
            cycle = True


for i in range(V):
    if not visited[i]:
        dfs(i, -1)

if cycle:
    print("'YES'")
else:
    print("'NO'")

print("task 3")

n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

vse = []
for i in range(n):
    vse.append([start[i], end[i]])

for i in range(n):
    for j in range(0, n - i - 1):
        if vse[j][1] > vse[j + 1][1]:
            vse[j], vse[j + 1] = vse[j + 1], vse[j]

count = 1
tu = vse[0][1]

for i in range(1, n):
    if vse[i][0] > tu:
        count += 1
        tu = vse[i][1]

print(count)

print("task 4")

V, E, start, end = input().split()
V = int(V)
E = int(E)

tun = {}
stat = []

for i in range(E):
    n1, n2, t = input().split()
    t = int(t)

    if n1 not in stat:
        stat.append(n1)
    if n2 not in stat:
        stat.append(n2)

    tun[(n1, n2)] = t
    tun[(n2, n1)] = t

matr = []
for i in range(V):
    row = []
    for j in range(V):
        if i == j:
            row.append(0)
        else:
            if (stat[i], stat[j]) in tun:
                row.append(tun[(stat[i], stat[j])])
            else:
                row.append(float("inf"))
    matr.append(row)

d = [float("inf")] * V
used = [False] * V
parent = [-1] * V

here = stat.index(start)
suda = stat.index(end)

d[here] = 0

for i in range(V):
    v = -1
    md = float("inf")
    for j in range(V):
        if not used[j] and d[j] < md:
            md = d[j]
            v = j

    if v == -1:
        break

    used[v] = True

    for j in range(V):
        if d[j] > d[v] + matr[v][j]:
            d[j] = d[v] + matr[v][j]
            parent[j] = v

ans = []
v = suda
while v != -1:
    ans.append(stat[v])
    v = parent[v]
ans.reverse()

with open('metro.txt', 'w') as f:
    f.write(f"Время в пути: {d[suda]} минут\n")
    f.write("Кратчайший путь: " + " -> ".join(ans))

print(d[suda])

print("task 5")

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

d = [-1] * n
queue = [0]
d[0] = 0

i = 0
while i < len(queue):
    v = queue[i]
    i += 1

    for j in g[v]:
        if d[j] == -1:
            d[j] = d[v] + 1
            queue.append(j)

for i in range(n):
    print(d[i])

print("task 6")

N = int(input())
M = int(input())

g = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * N


def dfs(v):
    visited[v] = True
    for to in g[v]:
        if not visited[to]:
            dfs(to)


k = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        k += 1

print(k)
