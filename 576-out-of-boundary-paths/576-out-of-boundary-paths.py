class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(maxsize = None)
        def sol(i , j , m , n , cnt):
            if cnt > maxMove:
                return 0 
            if i < 0 or i >= m or j < 0 or j >= n :
                return 1 
            a = sol(i + 1, j , m , n , cnt + 1 )
            b = sol ( i - 1 , j , m , n , cnt + 1)
            c = sol(i , j + 1 , m , n , cnt + 1)
            d = sol(i , j - 1, m , n , cnt + 1)
            return a + b + c + d 
        return sol(startRow , startColumn , m , n , 0) %(10** 9 + 7)