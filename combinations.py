from itertools import combinations
from itertools import permutations
d=[1,5,5,25,125]
q=list(permutations(d,3))
p=list(combinations(d,3))
for i in p:
      l=list(i)
      print(i)

