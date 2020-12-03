s = input('Введите символы: ')
l = len(s)
r = ''
for i in range(l):
    if l%(i+1) == 0:
        r += s[i]
print(r)
