print("task 1")

a = input()

spis = a.split("student_")
spis.remove("")
Mball = max([i[3:] for i in spis])
students = [i[:3] for i in spis if i[3:] == Mball]
for i in students: print(i, end=" ")

print("task 2")

a, b = map(int, input().split())

print(f"Длина окружности равна {round(2*3.1416*a, 2)}. Площадь круга составляет {round(((3.1416*(a**2))/(b**2))*100, 2)} % от площади квадрата.")

print("task 3")

a, b = map(str, input().split())

a = a[1] + a[0] + a[2:]
b = b[1] + b[0] + b[2:]
print(f"{a}-{b}")

print("task 4")

a = input()
k = 0
if len(a) > 3:
    for i in a[:5]:
        if i == i.upper():
            k += 1
    if k >= 3:
        print(a.upper())
    else:
        print(a)
else:
    print(a)

print()

print("task 5")

a = list(map(str, "a, abbr, b, body, caption, cite, code, div, form, h1, h2, h3, h4, h5, h6, header, i и s".split(", ")))

tag = input()
s = input()
if tag in a:
    print(f"<{tag}>{s}<{tag}>")
else:
    print("Введён неверный тег")

print("task 6")

b =  input()
a = len(b)
if a <= 2:
    print(ord(b[0]))
elif a > 2 and a < 10:
    print(ord(b[0])+ord(b[-1])+ord(b[int(a/2)-1]))
else:
    print(ord(b[-1]))

