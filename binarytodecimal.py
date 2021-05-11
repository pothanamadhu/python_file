binary=list(map(int,input().split()))
l=len(binary)-1
k=l
s=0
i=0
while(l!=-1):
      s=s+(binary[l]*(2**i))
      i=i+1
      l=l-1
print(s)
      
