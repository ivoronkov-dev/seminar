import unittest

print("task 1")


a = int(input())

def simple(x):
    b = []
    prov = 2
    while prov**2 <= x:
        if x % prov == 0:
            x = x / prov
            b.append(prov)
        else:
            prov+=1
    if x != 1:
        b.append(int(x))
    return b

def test1():
    case = unittest.TestCase()
    try:
        result = simple(4)
        case.assertEqual(result, [2, 2], "окак")
        print("Тест 1 прошел успешно!")
    except AssertionError as e:
        print(f"Тест 1 не прошел: {e}")

def test2():
    case = unittest.TestCase()
    try:
        result = simple(111)
        case.assertEqual(result, [3, 37], "окак")
        print("Тест 2 прошел успешно!")
    except AssertionError as e:
        print(f"Тест 2 не прошел: {e}")

def test3():
    case = unittest.TestCase()
    try:
        result = simple(101)
        case.assertEqual(result, [101], "окак")
        print("Тест 3 прошел успешно!")
    except AssertionError as e:
        print(f"Тест 3 не прошел: {e}")

test1()
test2()
test3()
print("Вывод программы: ", simple(a))

print("task 2")

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
def mnk(x, y):
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
    return a, b



def test4():
    case = unittest.TestCase()
    try:
        result = mnk([1, 4, 8, 10, 15], [2, 4, 10, 5, 7])
        case.assertEqual(result, (0.343, 2.993), "окак")
        print("Тест 1 прошел успешно!")
    except AssertionError as e:
        print(f"Тест 1 не прошел: {e}")

def test5():
    case = unittest.TestCase()
    try:
        result = mnk([1, 3, 1, 4, 1], [2, 0, 9, 0, 1])
        case.assertEqual(result, (-1.5, 5.4), "окак")
        print("Тест 2 прошел успешно!")
    except AssertionError as e:
        print(f"Тест 2 не прошел: {e}")

test4()
test5()
print("Вывод программы: ", mnk(x, y))

print("task 3")

def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quick_sort(L) + M + quick_sort(R)

try:
    assert quick_sort("123".split()) == ['123'], "должно быть [1, 2, 3]"
    assert len(quick_sort("123".split())) == 1, "функция меняет данные!"
except AssertionError as e:
    print(f"В коде ошибка: {e}")

print(quick_sort(input().split()))


print("task 4")

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, ovechka):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + ovechka) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i + ovechka) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


try:
    testik = Caesar(19)
    assert testik.decode("Ыетэ, фн цбхтцтюыдо вбйчяё кыжг") == "Итак, вы догадались почему шифр", "он не работает("
except AssertionError as e:
    print(f"В коде ошибка: {e}")

key = int(input('Введите ключ(рекомендую 19):'))
cipher = Caesar(key)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()





