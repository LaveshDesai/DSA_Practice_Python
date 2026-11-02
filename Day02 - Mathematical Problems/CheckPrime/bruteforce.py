class Solution:
    def checkPrime(self,n:int)->bool:
        if n<=1: #it will check negative,0 and 1
            return False
        
        for i in range(2,n):
            if n%i==0:
                return False
           
        return True
        
        
        
        
        
        
        
        
        
        
        
s = Solution()
print(s.checkPrime(12))
