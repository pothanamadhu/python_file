def mad(s):
    d={}
    n=len(s)
    k=0
    for g in range(n):
        i=g+1
        j=0
        if i==1:
            k=len(list(set(s)))
        else:
            while i<=len(s):
                l=s[j:i]
                if l not in d.keys():
                    d[l]=1
                i=i+1
                j=j+1
    return k+len(d)
def countSubstrings(s, queries):
    lik=[]
    for m in queries:
        if m[0]==m[1]:
            lik.append(1)
        else:
            k=mad(s[m[0]:m[1]+1])
            lik.append(k)
    return lik
n,m=map(int,input().split())
data=input()
b=[]
for i in range(m):
      d=list(map(str,input().split()))
      b.append(d)
k=countSubstrings(data,b)
print(k)








      
