dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60} 
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
n=0
for i in dic4:
    a=i*dic4[i]
    n+=a
print(n)
