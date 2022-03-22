def lower(d,t):
      l,r=0,len(d)-1
      while l<=r:
            m=(l+r)//2
            if d[m]>=t:
                  r=m-1
            else:
                  l=m+1
      return l
def upper(d,t):
      l,r=0,len(d)-1
      while l<=r:
            m=(l+r)//2
            if d[m]>t:
                  r=m-1
            else:
                  l=m+1
      return r
d=list(map(int,input().split()))
t=int(input())
d.sort()
l=lower(d,t)
r=upper(d,t)
d=[i for i in range(l,r+1)]
print(d)
