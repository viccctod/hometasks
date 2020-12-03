lst=[0]*3
lst[0]=31
lst[1]=24
lst[2]=17
a=[]
th=[]
f=[]
print (lst)

f=lst+a+th+f
a=f
print (a)

f=f+a
for i in range (2):
    th.append(int(input("Введите символы: ")))
print (th)

f=th+a+lst
print (f)
