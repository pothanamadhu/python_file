def reverse(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s 
m=int(input())
n=int(input())
k=m 
mrev=reverse(n)
k=m
p=0
while(mrev):
      p=mrev%10
      mrev=mrev//10
      k=k*10+p
print("by concatinating",n,"&",m,"we got",k)
      
