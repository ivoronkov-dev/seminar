import collections
import sys
from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        """Построение слоистой сети."""
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = collections.deque([s])
        while queue:
            u = queue.popleft()
            for v, cap, rev_idx in self.graph[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, flow, ptr):
        """Поиск блокирующего потока в слоистой сети."""
        if u == t or flow == 0:
            return flow

        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f


n = int(input())
while n != 0:

    s, t, c = map(int, input().split())
    dinic = Dinic(n + 1)
    for i in range(c):
        a, b, d = map(int, input().split())
        dinic.add_edge(a, b, d)
        dinic.add_edge(b, a, d)

    print(f"Максимальный поток (Диниц): {dinic.max_flow(s, t)}")
    n = int(input())
    if n == 0:
        break

inf = float("inf")


# спасибо за помощь Deepseek

def min_cost_flow(cost_matrix, n_sources, n_targets):
    n = n_sources + n_targets + 2
    s = 0
    t = n - 1
    cap = [[0] * n for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    for i in range(1, n_sources + 1):
        cap[s][i] = 1
    for j in range(1, n_targets + 1):
        cap[n_sources + j][t] = 1
    for i in range(n_sources):
        for j in range(n_targets):
            u = i + 1
            v = n_sources + j + 1
            cap[u][v] = 1
            cost[u][v] = cost_matrix[i][j]
            cost[v][u] = -cost_matrix[i][j]

    total_flow = 0
    total_cost = 0
    while total_flow < n_sources:
        dist = [inf] * n
        inqueue = [False] * n
        parent = [-1] * n
        parent_edge = [-1] * n
        dist[s] = 0
        q = deque([s])
        inqueue[s] = True
        while q:
            u = q.popleft()
            inqueue[u] = False
            for v in range(n):
                if cap[u][v] > 0 and dist[v] > dist[u] + cost[u][v]:
                    dist[v] = dist[u] + cost[u][v]
                    parent[v] = u
                    parent_edge[v] = (u, v)
                    if not inqueue[v]:
                        q.append(v)
                        inqueue[v] = True
        if dist[t] == inf:
            break
        v = t
        while v != s:
            u, _ = parent_edge[v]
            cap[u][v] -= 1
            cap[v][u] += 1
            v = u
        total_flow += 1
        total_cost += dist[t]
    return total_cost


def solve():
    numbers = list(map(int, sys.stdin.read().split()))

    idx = 0
    t = numbers[idx]
    idx += 1
    out_lines = []

    for _ in range(t):
        n = numbers[idx]
        idx += 1

        cnt = [0] * (n + 1)
        for __ in range(n):
            card = numbers[idx]
            idx += 1
            cnt[card] += 1

        e = numbers[idx]
        idx += 1

        adj = [[] for _ in range(n + 1)]
        for __ in range(e):
            a = numbers[idx]
            b = numbers[idx + 1]
            idx += 2
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * (n + 1)
        components = []
        for v in range(1, n + 1):
            if not visited[v]:
                stack = [v]
                visited[v] = True
                comp = []
                while stack:
                    u = stack.pop()
                    comp.append(u)
                    for w in adj[u]:
                        if not visited[w]:
                            visited[w] = True
                            stack.append(w)
                components.append(comp)

        total_swaps = 0
        for comp in components:
            sources = []
            targets = []
            for v in comp:
                if cnt[v] > 1:
                    sources.extend([v] * (cnt[v] - 1))
                elif cnt[v] == 0:
                    targets.append(v)

            if not sources:
                continue

            size = len(comp)
            idx_map = {v: i for i, v in enumerate(comp)}
            dist = [[-1] * size for _ in range(size)]

            for i, start in enumerate(comp):
                q = [start]
                dist[i][i] = 0
                qpos = 0
                while qpos < len(q):
                    u = q[qpos]
                    qpos += 1
                    du = dist[i][idx_map[u]]
                    for w in adj[u]:
                        if dist[i][idx_map[w]] == -1:
                            dist[i][idx_map[w]] = du + 1
                            q.append(w)

            d = len(sources)
            cost_mat = [[0] * d for _ in range(d)]
            for si, s_val in enumerate(sources):
                si_idx = idx_map[s_val]
                for ti, t_val in enumerate(targets):
                    ti_idx = idx_map[t_val]
                    cost_mat[si][ti] = dist[si_idx][ti_idx]

            total_swaps += min_cost_flow(cost_mat, d, d)

        out_lines.append(str(total_swaps))

    print("\n".join(out_lines))


if __name__ == "__main__":
    solve()
