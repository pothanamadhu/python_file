def reverse(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
def isodd(n):
      if(n%2!=0):
            return True
      else:
            return False
n=int(input())
num=isodd(n)
rev=reverse(n)
numrev=isodd(rev)
if(num and numrev):
      print("co-odd")
else:
      print("not a co-odd")
      
