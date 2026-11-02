# Count Number of Odd Digits in a Number

## Optimal Approach: Extract Digits Using Modulo

In this approach, I extract each digit using `% 10` and check whether it is odd. If the digit is odd, I increase the count.

### Code

```python
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
```

### Example

```python
Input:    -45231
Output:   3
Expected: 3
```

### Why it Works

I extract the last digit using `% 10`, check if it is odd, and remove the last digit using `// 10`. This continues until all digits are processed.

### Complexity

- **Time Complexity: O(log n)** → The loop runs once for each digit in the number.
- **Space Complexity: O(1)** → Only a few variables are used.

### Interview Follow-up Questions

**1. Why is `% 10` used?**  
→ `% 10` gives the last digit of a number.

**2. Why use `num % 2 != 0` instead of `num % 2 == 1`?**  
→ `!= 0` directly checks for odd numbers and works consistently for all integer values.

**3. What happens when the input is `0`?**  
→ The function returns `0` because the number `0` contains no odd digits.
