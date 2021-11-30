n=int(input())
possible,remaining=n//7,n%7
print(int(possible*28+(((possible-1)*possible)/2)*7+((possible+remaining)*(possible+remaining+1))/2-((possible)*(possible+1))/2)
