m=[]
for i in range(5):
      k=list(map(int,input().split()))
      m.append(k)
for i in range(5):
      for j in range(5):
            if m[i][j]==1:
                  p=i+1
                  q=j+1
                  break
p=abs(p-3)
q=abs(q-3)
print(p+q)
      
      
