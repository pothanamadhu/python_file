n=int(input())
for i in range(n):
      m=input()
      if len(m)>10:
            k=str(len(m)-2)
            m=m[0]+k+m[-1]
      print(m)
