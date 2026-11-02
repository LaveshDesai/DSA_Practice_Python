class Solution:
    def countOdd(self, x: int) -> int:
        if x < 0:
            x = abs(x)
        elif x == 0:
            return 0

        count = 0

        while x > 0:
            num = x % 10

            if num % 2 != 0:
                count += 1

            x //= 10

        return count
