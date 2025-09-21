import numpy as np
import random
print("task 1")
n = int(input())
x = [0, 1, 1]
for i in range(n):
    x[0] = x[1]
    x[1] = x[2]
    x[2] = x[0] + x[1]
print(x[-3])


print("task 2")
a = int(input())
b = []
prov = 2
while prov**2 <= a:
    if a % prov == 0:
        a = a / prov
        b.append(prov)
    else:
        prov+=1
if a != 1:
    b.append(int(a))
print(b)

print("task 3")
# спасибо за помощь deepseek
a, b = map(int, input().split())
def f(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = f(b, a % b)
    return y1, x1 - (a // b) * y1, d
x, y, d = f(a, b)
print(x, y, d)


print("task 4")

syze = int(input())

symb = input()
r = symb
if syze % 2 == 1:
    for i in range(syze//2 + 1):
        print(r)
        r += symb
    r = r[1::]
    for i in range(syze//2):
        r = r[1::]
        print(r)
if syze % 2 == 0:
    for i in range(syze//2 + 1):
        print(r)
        r += symb
    for i in range(syze//2):
        r = r[1::]
        print(r)
    print(symb)

print("task 5")
# спасибо за помощь deepseek
def spiral_matrix(n, m):
    matrix = np.zeros((n, m), dtype=int)
    top, bottom, left, right = 0, n - 1, 0, m - 1
    num = 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix
n, m = map(int, input().split())
matrix = spiral_matrix(n, m)
result = np.zeros_like(matrix)
for i in range(n):
    result[i] = matrix[i] * (i + 1)
print(result)


print("task 6")
# сюда нужно ввести измерения x и y
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
xy = []
x2 = []
sy = sum(y)
sx = sum(x)

for i in range(len(x)):
    xy.append(x[i] * y[i])
    x2.append(x[i]**2)
sxy = sum(xy)
sx2 = sx**2

a = round((len(x) * sxy - sx * sy) / (len(x) * sum(x2) - sx2), 3)
b = round((sy - a * sx) / len(x), 3)

print(a, b)

print("task 7")
# тут помог deepseek
def easy():
    N = int(input("N: "))
    M = int(input("M: "))
    matrix = []
    for i in range(N):
        row = list(map(float, input().split()))
        matrix.append(row)
    A = np.array(matrix)
    coefficients = A[:, :-1]
    constants = A[:, -1]
    solution = np.linalg.solve(coefficients, constants)
    return solution
print(easy())


print("task 8")
# с генерацией помог deepseek
def some_dots(N, noise_std=1.0, x_range=(0, 10)):
    a = random.randrange(-20, 20)
    b = random.randrange(-10, 10)
    print("Истинные коэффициенты:", a, b)
    x_min, x_max = x_range
    x = np.linspace(x_min, x_max, N)

    y_ideal = a * x + b

    y = np.array([random.gauss(y_i, noise_std) for y_i in y_ideal])

    return x, y
x, y = some_dots(int(input("Количество точек: ")))
xy = []
x2 = []
sy = sum(y)
sx = sum(x)

for i in range(len(x)):
    xy.append(x[i] * y[i])
    x2.append(x[i]**2)
sxy = sum(xy)
sx2 = sx**2

a = round((len(x) * sxy - sx * sy) / (len(x) * sum(x2) - sx2), 3)
b = round((sy - a * sx) / len(x), 3)

print("Результат:", a, b)