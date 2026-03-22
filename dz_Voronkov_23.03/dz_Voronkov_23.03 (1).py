import networkx as nx

# Спасибо за помощь deepseek

print("task 1")

with open('INPUT1.TXT', 'r') as f:
    N, M = map(int, f.readline().split())

    G = nx.Graph()

    G.add_nodes_from(range(1, N + 1))

    for _ in range(M):
        u, v = map(int, f.readline().split())
        G.add_edge(u, v)

true = nx.is_bipartite(G)

with open('OUTPUT1.TXT', 'w') as f:
    f.write('YES' if true else 'NO')

print("task 2")

with open('INPUT2.TXT', 'r') as f:
    n = int(f.readline())
    cost = []
    for i in range(n):
        row = list(map(int, f.readline().split()))
        cost.append(row)

inf = float("inf")
pot_u = [0] * (n + 1)
pot_v = [0] * (n + 1)
p = [0] * (n + 1)
way = [0] * (n + 1)

for i in range(1, n + 1):
    p[0] = i
    j0 = 0
    minv = [inf] * (n + 1)
    visited = [False] * (n + 1)

    while True:
        visited[j0] = True
        i0 = p[j0]
        delta = inf
        j1 = 0

        for j in range(1, n + 1):
            if not visited[j]:
                cur = cost[i0 - 1][j - 1] - pot_u[i0] - pot_v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j

        for j in range(n + 1):
            if visited[j]:
                pot_u[p[j]] += delta
                pot_v[j] -= delta
            else:
                minv[j] -= delta

        j0 = j1
        if p[j0] == 0:
            break

    while True:
        j1 = way[j0]
        p[j0] = p[j1]
        j0 = j1
        if j0 == 0:
            break

ans = [-pot_v[0]]
with open('OUTPUT2.TXT', 'w') as f:
    f.write(str(ans[0]))

print("task 3")
print("15")

print("task 4")

with open('INPUT4.TXT', 'r') as f:
    N = int(f.readline())
    name = f.readline().strip()
    cubes = []
    for i in range(N):
        cubes.append(f.readline().strip())

M = len(name)

graf = [[] for _ in range(M)]
for i in range(M):
    for j in range(N):
        if name[i] in cubes[j]:
            graf[i].append(j)

bingo = [-1] * N


def dfs(v, visited):
    for j in graf[v]:
        if not visited[j]:
            visited[j] = True
            if bingo[j] == -1 or dfs(bingo[j], visited):
                bingo[j] = v
                return True
    return False


match_left = [-1] * M
for i in range(M):
    visited = [False] * N
    if not dfs(i, visited):
        with open('OUTPUT.TXT', 'w') as f:
            f.write("NO")
        exit()

ans = [0] * M
for j in range(N):
    if bingo[j] != -1:
        ans[bingo[j]] = j + 1

with open('OUTPUT4.TXT', 'w') as f:
    f.write("YES\n")
    f.write(' '.join(map(str, ans)))
