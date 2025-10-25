print("task 1")

# Тут помог deepseek
def barashek(okak):

    def chitabelno(z):
        zn = []
        i = 0
        while i < len(z):
            if z[i].isspace():
                i += 1
                continue
            if z[i] in '()+-*/':
                zn.append(z[i])
                i += 1
            elif z[i].isdigit():
                num = ''
                while i < len(z) and z[i].isdigit():
                    num += z[i]
                    i += 1
                zn.append(num)
            else:
                i += 1
        return zn

    def bebebe(zn):
        poradok = {'+': 1, '-': 1, '*': 2, '/': 2}
        op = []
        och = []

        for i in zn:
            if i.isdigit():
                op.append(i)
            elif i == '(':
                och.append(i)
            elif i == ')':
                while och and och[-1] != '(':
                    op.append(och.pop())
                och.pop()
            else:
                while (och and och[-1] != '(' and
                       poradok.get(och[-1], 0) >= poradok[i]):
                    op.append(och.pop())
                och.append(i)

        while och:
            op.append(och.pop())

        return ' '.join(op)

    def bububu(zn):
        r_zn = []
        for i in reversed(zn):
            if i == '(':
                r_zn.append(')')
            elif i == ')':
                r_zn.append('(')
            else:
                r_zn.append(i)

        bebebe_r = bebebe(r_zn)
        bububu = ' '.join(reversed(bebebe_r.split()))
        return bububu

    zn = chitabelno(okak)
    bebebebe = bebebe(zn)
    bubububu = bububu(zn)

    return bebebebe, bubububu


okak = input("Жду ваше выражение: ")
bebebebe, bubububu = barashek(okak)

print(f"Обратная польская: {bebebebe}")
print(f"Прямая польская: {bubububu}")


print("task 2")


def krosh(okak):
    c = okak.split()
    och = []

    for i in c:
        if i.isdigit():
            och.append(int(i))
        else:
            b = och.pop()
            a = och.pop()

            if i == '+':
                o = a + b
            elif i == '-':
                o = a - b
            elif i == '*':
                o = a * b
            elif i == '/':
                if b == 0:
                    return "Зачем вы делите на ноль, я не умею такое считать :((((((((("
                o = a / b
            else:
                return "ААА, ВСЁ ПРОПАЛО, в выражении оШиБкА!"

            och.append(o)
    if len(och) == 1:
        return och[0]


print(krosh(input("Жду ваше выражение: ")))

print("task 3")

def pin(okak):
    expr = okak.replace(" ", "")

    poradok = {'+': 1, '-': 1, '*': 2, '/': 2}

    out = []
    och = []
    i = 0
    while i < len(expr):
        char = expr[i]

        if char in '0123456789':
            num = char
            while i + 1 < len(expr) and expr[i + 1] in '0123456789':
                i += 1
                num += expr[i]
            out.append(num)

        elif char == '(':
            och.append(char)

        elif char == ')':
            while och and och[-1] != '(':
                out.append(och.pop())
            och.pop()

        elif char in '+-*/':
            while (och and och[-1] != '(' and
                   poradok[och[-1]] >= poradok[char]):
                out.append(och.pop())
            och.append(char)
        i += 1

    while och:
        out.append(och.pop())

    return ' '.join(out)

print(pin(input("Waiting for your equation: ")))
