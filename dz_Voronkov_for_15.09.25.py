print("task 1")
a = list(map(int, input().split()))
for i in range(1, a[0]):
    if i not in a:
        print(i)
        break

print("task 2")
a = list(input().split())
print(a)
r = ""
shag = int(len(a[1])/int(a[0]))
print(shag)
for i in range(int(a[0])):
    r = r + a[1][shag-1:0:-1]
    r = r + a[1][0]
    a[1] = a[1][shag:]
print(r)

print("task 3")
s = input()
slov = {'A':'A','E':'3','3':'E','H':'H','I':'I','J':'L','L':'J','M':'M','O':'O','S':'2','2':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'5','5':'Z','1':'1','8':'8'}
pal = (s == s[::-1])
mir = True
n = len(s)
for i in range(n):
    a = s[i]
    b = s[n-1-i]
    if a not in slov or slov[a] != b:
        mir = False
        break
if pal and mir:
    print(f'"{s}" is a mirrored palindrome.')
elif pal:
    print(f'"{s}" is a regular palindrome.')
elif mir:
    print(f'"{s}" is a mirrored string.')
else:
    print(f'"{s}" is not a palindrome.')

print("task 4")
a = input().split()
for i in range(0, len(a)-1, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(' '.join(a))

print("task 5")
a = input()
print(a[-1] + a[:-1])

print("task 6")
a = list(map(int, input().split()))
for i in a:
    if a.count(i) == 1:
        print(i, end=' ')

print("task 7")
schet = 0
k = -1
a = list(map(int, input().split()))
for i in a:
    if a.count(i) > schet:
        schet = a.count(i)
        k = i
print(k)

print("task 8")
n = int(input())
a = list(map(int, input().split()))
for i in range(0, int(n/2 - 0.5)):
    a.pop(a.index(max(a)))
print(max(a))

print("task 9")
with open('input.txt', 'r') as f1:
    a = str(f1.readlines())
print(a.count('. ') + a.count('! ') + a.count('? ') + 1)


print("task 10")
s = input()
spis = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
k = "а"
ans = ""
for let in s:
    if let in spis and k not in spis:
        k = let
        ans = ans + let + "с" + let
    else:
        k = let
        ans = ans + let
print(ans)


