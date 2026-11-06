class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)


        for i in range(n-1): # i should be smaller than j traversing over to last element of an array
          for j in range(i+1,n): # it will start from one index ahead of i
            total = numbers[i]+numbers[j]

            if total==target:
              return [i+1,j+1]
            
         
                    
