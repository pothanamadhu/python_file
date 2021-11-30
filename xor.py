l,h,k=map(int,input().split())
n=p=0
for i in range(l,h):
      for j in range(l+1,h):
            if i!=j:
                  g=i^j
                  if g<=k:
                        n=g
                  else:
                        break
                        p=1
      if p==1:
            break
print(n)
                        
                 
