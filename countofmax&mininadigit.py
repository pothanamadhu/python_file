n=int(input())
ma=n%10
mi=n%10
mic=0
mac=0
while n:
      r=n%10
      n=n//10
      if r==mi:
            mic+=1
      elif r<mi:
            mi=r
            mic=1
      if r==ma:
            mac+=1
      elif r>ma:
            ma=r
            mac=1
print("min",mi,mic)
print("max",ma,mac)
