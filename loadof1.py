n=int(input())
data=list(map(int,input().split()))
k=p=m=r=h=0
for i in range(0,n):#1 2 3 1 1 1 4
      if data[i]==1:
           k=k+1
           r=r+1
      else:
            if p<k:
                  p=k
                  k=0
                  h=i-1
                  m=i-r
                  r=0
p=max(k,p)
print(p)
print(m,h)
      

