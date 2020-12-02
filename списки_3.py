lst=["input","string","repeat",3]
if "repeat" in lst and type(lst[-1])==int:
    a=lst[:-2]*lst[-1]+lst[-2:]
print (a)
