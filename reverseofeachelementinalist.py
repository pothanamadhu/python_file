def reverse(data,n):
      r=0
      s=0
      for i in range(n):
            k=data[i]
            while(k):
                  r=k%10
                  k=k//10
                  s=s*10+r
            data[i]=s
            s=0
n=int(input())
data=list(map(int,input().split()))
reverse(data,n)
for i in data:
      print(i,end=" ")

 
