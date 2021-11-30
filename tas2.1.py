n=int(input())
t=0
k=n**2
while k:
      r=k%10
      k=k//10
      t=t+r
if t==n:
      print("Neon Number")
else:
      print("Not Neon Number")
