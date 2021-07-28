def swap(n):
      n=list(n.split())
      m=[]
      for wor in range(len(n)):
            k=[]
            for i in n[wor]:
                  if i==i.upper():
                        k.append(i.lower())
                  else:
                        k.append(i.upper())
            m.append("".join(k))
      m.reverse()
      print(" ".join(m))
n=input()
swap(n)
