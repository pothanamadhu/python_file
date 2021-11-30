data=["g","r","e","e","s","s","e","g","1","1","1","1"]
d={}
d1={}
for i in data:
      if i not in d.keys():
            d[i]=1
      else:
            d[i]+=1
for k,v in d.items():
      if v not in d1.keys():
            d1[v]=[k]
      else:
            d1[v].append(k)
k=list(d1.keys())
g=[]
k=(sorted(k,reverse=True))
for i in k:
      for j in d1[i]:
            for n in range(i):
                  g.append(j)
print("".join(g))
      

      
