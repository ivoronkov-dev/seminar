import math

print("task 1")

n = int(input())
a = list(map(int, input().split()))
k = int(input())

s = 1
while s < n:
    s *= 2
tree = [0] * (2 * s)

for i in range(n):
    tree[s + i] = a[i]
for i in range(n, s):
    tree[s + i] = 0

for i in range(s - 1, 0, -1):
    tree[i] = max(tree[2 * i], tree[2 * i + 1])


def _max(le, r):
    le += s
    r += s
    now = 0
    while le <= r:
        if le % 2 == 1:
            now = max(now, tree[le])
            le += 1
        if r % 2 == 0:
            now = max(now, tree[r])
            r -= 1
        le //= 2
        r //= 2
    return now


c = []
for i in range(k):
    left, right = map(int, input().split())
    c.append(_max(left - 1, right - 1))

print(' '.join(map(str, c)))

print("task 2")

n = int(input())
a = list(map(int, input().split()))
k = int(input())

s = 1
while s < n:
    s *= 2
tree = [0] * (2 * s)

for i in range(n):
    tree[s + i] = a[i]
for i in range(n, s):
    tree[s + i] = 0

for i in range(s - 1, 0, -1):
    tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])


def _gcd(le, r):
    le += s
    r += s
    now = 0
    while le <= r:
        if le % 2 == 1:
            now = math.gcd(now, tree[le])
            le += 1
        if r % 2 == 0:
            now = math.gcd(now, tree[r])
            r -= 1
        le //= 2
        r //= 2
    return now


c = []
for i in range(k):
    left, right = map(int, input().split())
    c.append(_gcd(left - 1, right - 1))

print(' '.join(map(str, c)))

print("task 3")

n = int(input())
a = list(map(int, input().split()))
m = int(input())

size = 1
while size < n:
    size *= 2
tree = [0] * (2 * size)

for i in range(n):
    tree[size + i] = 1 if a[i] == 0 else 0
for i in range(n, size):
    tree[size + i] = 0

for i in range(size - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]


def _sum(le, r):
    le += size
    r += size
    vot = 0
    while le <= r:
        if le % 2 == 1:
            vot += tree[le]
            le += 1
        if r % 2 == 0:
            vot += tree[r]
            r -= 1
        le //= 2
        r //= 2
    return vot


def zero(le, r, k):
    nowl = le
    nowr = r
    nowx = 1

    while nowx < size:
        left = 2 * nowx
        right = 2 * nowx + 1

        mid = (nowl + nowr) // 2
        lef = _sum(nowl, mid)

        if lef >= k:
            nowx = left
            nowr = mid
        else:
            k -= lef
            nowx = right
            nowl = mid + 1

    return nowl + 1


results = []
for i in range(m):
    left, right, k = map(int, input().split())
    results.append(zero(left - 1, right - 1, k))

print(' '.join(map(str, results)))
