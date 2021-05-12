n=int(input())
data=list(map(int,input().split()))
k=0
l=0
for i in range(1,n):
      if(data[i-1]>data[i]):
            k=k+1
      elif(data[i-1]<data[i]):
            l=l+1
      if(k and l):
            print("False")
            break
else:
      print("True")
