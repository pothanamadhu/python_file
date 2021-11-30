n=int(input())
while n:
      if n%2==0 or n==1:
            n=n//2
      elif n%3==0:
            n=n//3
      elif n%5==0:
            n=n//5
      else:
            print("not ugly number")
            break
else:
      print("ugly num")
