max_val=int(input("ввести целое положительное число: "))
repeat=int(input("ввести целое положительное число: "))
lst=[]
for i in range (1,max_val+1):
    lst.append (i)
print (lst*repeat)
