class Solution:
    def checkPrime(self,n:int)->bool:
        if n<=1: #it will check negative,0 and 1
            return False
        if n ==2:
            return True
        if n%2==0:
            return False
        
        i =3
        
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True


s = Solution()
print(s.checkPrime(2))
        
        
        

