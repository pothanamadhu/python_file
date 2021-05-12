n=int(input())
for i in range(1,n+1):
      if n%i==0:
            if i*(i+1)==n:
                  print("pronic number")
                  break
else:
      print("not a pronic number")
      
      
