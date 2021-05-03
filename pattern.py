n=int(input())
k=n
for i in range(1,n+1):
      for j in range(1,i+1):
            if(j<i):
                  print(" ",end=" ")
            else:
                  print(n+i-j,end=" ")
      print("\n")
      
