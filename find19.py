n=int(input())
data=list(map(int,input().split()))
m=int(input())
k=j=0
for num in data:
      if m+num>=k:
            k=m+num
for num in data:
      if m*num>=j:
            j=m*num
print("sum",k)
print("mul",j)

      
      
      
