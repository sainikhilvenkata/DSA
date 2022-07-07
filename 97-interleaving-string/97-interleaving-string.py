class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) < len(s2):
            s2, s1 = s1, s2
        dp = [""] * (len(s2)+1)
        
        for i in range(1, len(s2)+1):
            dp[i] = dp[i-1] + s2[i-1]
       
        tmp = dp[:]
        for i in range(1, len(s1)+1):
            dp[0] = dp[0] + s1[i-1]
            for j in range(1, len(s2)+1):
                if s3[:i+j] == tmp[j] + s1[i-1]:
                    dp[j] = tmp[j] + s1[i-1]
                elif s3[:i+j] == dp[j-1] + s2[j-1]:
                    dp[j] = dp[j-1] + s2[j-1]
                else:
                    dp[j] = ""
            tmp = dp[:]

        return dp[-1] == s3
            
        