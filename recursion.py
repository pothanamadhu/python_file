def sums(n):
      if n==1:
            return 1
      return n+sums(n-1)
n=int(input())#5
k=sums(n)
print(k)
