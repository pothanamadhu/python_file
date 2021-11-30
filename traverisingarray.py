n=int(input())
data=list(map(int,input().split()))
for i in range(n):
      for j in range(i+1,n):
            print(data[i],data[j])
