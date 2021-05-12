def pronic(n):
      for i in range(1,n+1):
            if n%i==0:
                  if i*(i+1)==n:
                        return True
      else:
            return False
n=int(input())
for i in range(1,n+1):
      if(pronic(i)):
            print(i)

      
      
