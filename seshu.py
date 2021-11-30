n=int(input())
i=0
j=1
k=0
y=2
p=1
if(n==1 or n==2):
      print(n-1)
else:
      while y!=n:
            k=i+j#1,2,3,5
            i=j#1,1,2,3
            j=k#1,2,3,5
            y=y+1#3,4,5,6
            p=p+k#2,4,7,12
      print(p)
