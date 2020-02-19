t=(1,1,2,3,5,5)
b=[]
for i in t:
    if t.count(i)>1 and i not in b:
         print(i)
         b.append(i)
