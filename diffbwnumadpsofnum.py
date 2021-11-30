import math
n=int(input())
s=int(math.sqrt(n))
if (n-s**2>(s+1)**2-n):
      print((s+1)**2-n)
else:
      print(n-s**2)
