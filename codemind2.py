n=int(input())
data=list(map(int,input().split()))
d={}
for i in data:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
p=[]
for k,v in d.items():
    if v==1:
        p.append(k)
p.sort()
print(*p)
