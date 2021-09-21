def lh(n):
      i=k=0
      while i!=len(n)-1:
            if i%2==0 or i==0:
                  if not n[i]<n[i+1]:
                        k=k+1
                        i=i+1
            else:
                  if not n[i]>n[i+1]:
                        k=k+1
                        i=i+1
            if i==len(n)-1:
                              break
            i=i+1
      return k
def hl(n):
      i=k=0
      while i!=len(n)-1:
            if i%2==0 or i==0:
                  if not n[i]>n[i+1]:
                        k=k+1
                        i=i+1
            else:
                  if not n[i]<n[i+1]:
                        k=k+1
                        i=i+1
            if i==len(n)-1:
                              break
            i=i+1
      return k
n=list(map(int,input().split()))
k=lh(n)
g=hl(n)
print(min(k,g))
