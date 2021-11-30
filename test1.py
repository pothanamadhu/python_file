n=int(input())
data=list(map(int,input().split()))
maps={}
for i in data:
      if i not in maps.keys():
            maps[i]=1
      else:
            mps[i]+=1
for i in range(n):
      data[i]=n-maps[data[i]]
print(data)
      
      
