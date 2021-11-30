n=int(input())
d={}
for i in range(n):
      name=input()
      score=float(input())
      if name not in d.keys():
            d[name]=score
data=list(set(d.values()))
p=data[-2]
mad=[]
for k,v in d.items():
      if v==p:
            mad.append(k)
mad.sort()
print(mad)
"""n=input()
k=0
s=0
for i in n:
      if i.isdigit():
            s=s*10+int(i)
      else:
            k=k+s
            s=0
k=k+s
print(k)"""
