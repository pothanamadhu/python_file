n=int(input())
k=1
for i in range(1,n):
      for j in range(1,i):
            print(k,end=" ")
            k=k+1
            if k>n:
                  break
      if k>n:
            break
      print()
