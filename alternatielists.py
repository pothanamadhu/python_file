d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
d3=[]
k1=len(d1)
k2=len(d2)
i=0
while i<k1 or i<k2:
      if i<k1:
            d3.append(d1[i])
      if i<k2:
            d3.append(d2[i])
      i=i+1
print(*d3)
