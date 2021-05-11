n,r1,r2=map(int,input().split())
for i in range(1,r2+1):
      if(i*n%n==0 and i*n%r1!=0):
            print(i,n,i*n)
