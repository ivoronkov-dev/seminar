from collections import deque
from math import inf

print("Упражнение")
n = int(input())
graf = []
for i in range(n):
    graf.append(list(sorted(map(int, input().split()))))

kol = max([graf[x][1] for x in range(n)]) + 1

g = [[] for i in range(kol)]
for a, b in graf:
    g[a].append(b)
    g[b].append(a)
# graf - матрица смежности
# g - список смежности

"""У матрицы быстрее проверка/удаление рёбер
у списка быстрее обход графа, добавление вершин"""

print("task 1")
"""Представленный в условии тест первым аргументом выдаёт не количество
пар, а количество вершин, то есть правильный тест будет следующим:
Ввод:
5
0 1
1 2
2 3
3 5
4 1
Вывод:
True
"""
n = int(input())
graf = []

for i in range(n):
    graf.append(list(sorted(map(int, input().split()))))

kol = max([graf[x][1] for x in range(n)]) + 1

start = 0
g = [[] for i in range(kol)]
for a, b in graf:
    g[a].append(b)
    g[b].append(a)

visited = [False] * kol
prev = [None] * kol


def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)


dfs(start, visited, prev, g)
print(all(visited))

print("task 2")

kol = int(input())
graf = eval(input().strip())

start, kon = map(int, input().split())
g = [[] for i in range(kol)]
for a, b in graf:
    g[a].append(b)

visited = [False] * kol
prev = [None] * kol


def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)


dfs(start, visited, prev, g)
print(visited[kon])

print("task 3")
ans = []
slov = eval(input().strip())
graf = [(a, b) for a, b in slov.items()]
keys = [k for k in slov]

vals = [v for v in slov.values()]
print(keys)
print(vals)

for i in range(len(slov)):
    if vals[i] not in keys:
        ans.append(vals[i])
        k = i
        break
for j in range(len(slov)):
    if keys[j] not in vals:
        z = j
        break
for i in range(len(slov) - 1):
    ans.append(vals[vals.index(keys[k])])
    k = vals.index(keys[k])
print([keys[z]] + list(reversed(ans)))

print("task 4")

"""для связного неориентированного графа
рёбра = вершины - 1 => циклов нет, инчае
есть циклы, тогда:"""

k = int(input())
n = 0
while input() != "":
    n += 1
if n == (k - 1):
    print("False")
else:
    print("True")

print("task 5")

g = eval(input().strip())

start, end = map(int, input().split())

num = set()
for i, j, w in g:
    num.add(i)
    num.add(j)

kol = max(num) + 1

graf = [[] for _ in range(kol)]
for i, j, w in g:
    graf[i].append((j, w))

dist = [inf] * kol
dist[start] = 0
queue = deque([start])

while queue:
    i = queue.popleft()

    for j, weight in graf[i]:
        ndist = dist[i] + weight

        if ndist < dist[j]:
            dist[j] = ndist
            queue.append(j)

print(dist[end])

print("task 6")


def f(words):
    din = {}
    out = {}
    spis = {}

    num = set()
    for w in words:
        if w:
            num.add(w[0])
            num.add(w[-1])

    for n in num:
        din[n] = 0
        out[n] = 0
        spis[n] = []

    for w in words:
        if w:
            first = w[0]
            last = w[-1]

            out[first] += 1
            din[last] += 1
            spis[first].append(last)

    for n in num:
        if din[n] != out[n]:
            return False

    def dfs(start, visited):
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop()
            for neighbor in spis[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    start_n = words[0][0]

    visited = set()
    dfs(start_n, visited)

    for n in num:
        if n not in visited:
            if din[n] > 0 or out[n] > 0:
                return False

    return True


print(f(eval(input())))
