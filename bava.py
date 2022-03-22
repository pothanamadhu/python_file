n=input()
s=""
vowels=["a","e","i","o","y","u"]
n=n.lower()
for i in n:
      if i not in vowels:
            s=s+"."+i
print(s)
