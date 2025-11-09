print("task 1")

n = input("ВВедите массив в формате '[1, 2, 5, 10, 4]':")[1:-1].split(", ")
l2 = len(n)

Y = "1"
for i in range(l2):
    l1 = 2 * i + 1
    r1 = 2 * i + 2

    if l1 < l2 and n[l1] < n[i]:
        Y = "0"

    if r1 < l2 and n[r1] < n[i]:
        Y = "0"
print(Y)

print("task 2")

fran = input().split()
plov = input().split()
pian = input().split()
genii = []

for i in plov:
    if i in pian and i not in fran:
        genii.append(int(i))
print(sorted(genii))

print("task 3")

n = int(input())
slov = dict()
k = []
for i in range(n):
    f = input()
    if f not in slov:
        slov[f] = 1
    else:
        slov[f] += 1
for i in dict(sorted(slov.items(), key=lambda j: j[1], reverse=True)):
    print(i, slov[i])

print("task 4")

# Тут помогал deepseak

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

all = []
for i, s in enumerate(lst):
    for v in s:
        all.append((v, i))

all.sort()

c = {}
got = 0
l2 = 0
res = [0, 10 ** 9]

for i in range(len(all)):
    bebebe, j = all[i]
    c[j] = c.get(j, 0) + 1
    if c[j] == 1:
        got += 1

    while got == n and l2 <= i:
        if all[i][0] - all[l2][0] < res[1] - res[0]:
            res = [all[l2][0], all[i][0]]

        o_j = all[l2][1]
        c[o_j] -= 1
        if c[o_j] == 0:
            got -= 1
        l2 += 1

print(f"{res[0]}–{res[1]}")

print("task 5")


def f(a, n, i):
    now = i
    l2 = 2 * i + 1
    r = 2 * i + 2

    if l2 < n and a[l2] > a[now]:
        now = l2

    if r < n and a[r] > a[now]:
        now = r

    if now != i:
        a[i], a[now] = a[now], a[i]
        f(a, n, now)


def bar(lst):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        f(lst, n, i)

    for j in range(n - 1, 0, -1):
        lst[j], lst[0] = lst[0], lst[j]
        f(lst, j, 0)

    return lst


n = list(map(int, input().split()))
b = bar(n)
print(' '.join(map(str, b)))
