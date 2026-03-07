print("task 1 ")

n = int(input())

xy = []
for _ in range(n):
    x, y = map(float, input().split())
    xy.append((x, y))

ejs = []
for i in range(n):
    for j in range(i + 1, n):
        dist = ((xy[i][0] - xy[j][0]) ** 2 +
                (xy[i][1] - xy[j][1]) ** 2) ** 0.5
        ejs.append((i, j, dist))
        ejs.append((j, i, dist))

inf = float('inf')
dist = [inf] * n
dist[0] = 0.0

for i in range(n - 1):
    for u, v, w in ejs:
        if dist[u] != inf:
            new_dist = max(dist[u], w)
            if new_dist < dist[v]:
                dist[v] = new_dist

print(f"{dist[1]:.3f}")

print("task 2")

a = int(input())
for _ in range(a):
    n, m = map(int, input().split())

    inf = float("inf")

    dist = [[inf] * (n) for i in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i in range(m):
        x, y, t = map(int, input().split())
        dist[x][y] = t
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    b = True
    for i in range(n):
        if dist[i][i] < 0:
            b = False
    if b:
        print("невозможно")
    else:
        print("возможно")
