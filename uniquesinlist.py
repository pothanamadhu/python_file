def unique(n):
      u=[]
      while n:
            r=n%10
            n=n//10
            if r not in u:
                  u.append(r)
            else:
                  return 0
      return 1
data=list(map(int,input().split()))
c=0
for i in data:
      if unique(i):
            c=c+1
print(c)
