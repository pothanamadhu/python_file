def reverse(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
def iseven(n):
      if(n%2==0):
            return True
      else:
            return False
n=int(input())
num=iseven(n)
rev=reverse(n)
numrev=iseven(rev)
if(num and numrev):
      print("coeven")
else:
      print("not a coeven")
      
