class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m,n=len(num1)-1,len(num2)-1
        carry=0
        out=''
        while n>-1 or m>-1:
            i,j=0,0
            if m>-1:
                i=ord(num1[m])-ord('0')
                m-=1
            if n>-1:
                j=ord(num2[n])-ord('0')
                n-=1
           
            tmp=i+j+carry
            if tmp>9:
                carry=1
            else:
                carry=0
            tmp=str(tmp)
            out=tmp[-1]+out
        if carry==0:
            return out
        else:
            return "1"+out
            
        