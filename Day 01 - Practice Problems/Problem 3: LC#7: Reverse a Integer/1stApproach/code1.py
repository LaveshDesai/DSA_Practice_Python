class Solution:
  def reverse(self,x:int)->int:
    if x<0:
      sign = -1
    else:
      sign = 1
    rev = 0
    x = str(abs(x))
    rev = int(x[::-1]) * sign


    if rev < -2**31 or rev > 2**31 - 1:
      return 0
    else:
      return rev
    
