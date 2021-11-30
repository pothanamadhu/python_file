n=int(input())
d=list(map(int,input().split()))
even=[]
odd=[]
for i in d:
      if i%2==0:
            even.append(i)
      else:
            odd.append(i)
even.sort()
even.reverse()
odd.sort()
i=0
j=0
t=[]
for p in range(len(d)):
      if d[p]%2==0:
            t.append(even[i])
            i=i+1
      else:
            t.append(odd[j])
            j=j+1
print(*t)
