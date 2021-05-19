n=input()
d={}
for i in n:
      if i not in d.keys():
            d[i]=1
      else:
            d[i]+=1
g=0
p=[]
for k,v in d.items():
      if v>g:
            p.clear()
            p.append(k)
            g=v
      elif v==g:
            p.append(k)
print(*p)
