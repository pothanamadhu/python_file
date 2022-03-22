n=int(input())
m=int(input())
data=[]
for i in range(n):
      d=list(map(int,input().split()))
      data.append(d)
k=0
for word in data:
      for i in range(1,len(word)):
            if word[i-1]==word[i]:
                 if word[i]==1:
                        word[i]=0
                  else:
                        word[i]=1
                  k=k+1
print(k)
                  
            
