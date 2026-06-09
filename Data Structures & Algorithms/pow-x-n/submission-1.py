class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x,n*-1)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else:
            a = n//2
            b = n-a
            c = self.myPow(x,a)
            if a==b:
                return c*c
            else:
                
                return c*c*x