n=int(input())
m=int(input())
a=[]
for i in range(n):
      a.append(int(input()))
qu=[]
for i in range(m):
      f=list(map(int,input().split()))
      qu.append(f)
res=[]
for q in qu:
      if q[0]==0:
            a[q[1]]=q[2]
            res.append(0)
      else:
            for p in range(q[2]+1,len(a),1):
                  if a[p]>a[q[2]] and a[p] not in a[0:q[2]]:
                        res.append(a[p])
                        break
            else:
                  res.append(0)
ans=0
for i in res:
      ans=ans^i
print(ans)
                  
      
