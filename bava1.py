s=input()
v=["a","A","e","E","i","I","o","O","u","U"]
d=[]
for i in s:
      if i in v:
            d.append(i)
n=""
d.reverse()
k=0
for i in s:
      if i in v:
            n=n+d[k]
            k=k+1
      else:
            n=n+i
print(n)
      
