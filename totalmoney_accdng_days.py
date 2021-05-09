class Solution(object):
    def totalMoney(self, n):
        s=0
        extra=0
        if(1<=n<=1000):
            for i in range(1,n+1):
                if(i%7==1):
                    s=s+1+extra
                if(i%7==2):
                    s=s+2+extra
                if(i%7==3):
                    s=s+3+extra
                if(i%7==4):
                    s=s+4+extra
                if(i%7==5):
                    s=s+5+extra
                if(i%7==6):
                    s=s+6+extra
                if(i%7==0):
                    s=s+7+extra
                    extra+=1
            print(s)
