s1 = input('введите символы: ')
s2 = input('введите символы: ')
print('длина первой строки: ', len(s1), 'длина второй строки: ', len(s2))
if s1<s2:
    relation = 'перед'
else:
    relation = 'после'
print('cтрока ' + s1 + ' идет ' + relation + ' строки ' + s2)
