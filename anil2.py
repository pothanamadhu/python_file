def Minimumlength(n,m,a):
      a.sort()
      p=s=0
      mod=1000000007
      for i in range(n-1,-1,-1):
            p=p+(a[i]*2)
            s=s+1
            if s==m:
                  return p%mod
            for j in range(i-1,-1,-1):
                  p=p+(a[i]+a[j])
                  s=s+1
                  if s==m:
                        return p%mod
                  p=p+(a[i]+a[j])
                  s=s+1
                  if s==m:
                        return p%mod
      return -1
print(Minimumlength(3,3,[1,2,3]))
print(Minimumlength(2,3,[1,10]))
print(Minimumlength(3,1,[1,21,0]))
print(Minimumlength(1,2,[10]))
                  
                  
                  
                  
      
