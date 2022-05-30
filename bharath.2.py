n=int(input())
d=[]
for i in range(n):
      d.append(int(input()))
arr=[0]*n
arr[0]=1
for i in range(1,n):
      if d[i]>d[i-1]:
            arr[i]=arr[i-1]+1
      else:
            arr[i]=1
print(sum(arr))
