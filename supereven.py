def iseven(n):
      if(n%2==0):
            return True
      else:
            return False
n=int(input())
k=iseven(n)
p=0
if(k):
      print("even number")
      for x in range(1,n+1):
            if(x%2==0):
                  p+=1
      if(iseven(p)):
            print("super even number")
      else:
            print("not a super e en number")
else:
      print("not a even number")
