def findevenpos(data,n):
      for i in range(n):
            if(data[i]%2==0):
                  return i
n=int(input())
data=list(map(int,input().split()))
k=findevenpos(data,n)
print(k)

