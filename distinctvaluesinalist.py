def distinct(data,n):
      tata=[]
      for i in data:
            if data.count(i)==1:
                  tata.append(i)
      print(*tata)
n=int(input())
data=list(map(int,input().split()))
distinct(data,n)
