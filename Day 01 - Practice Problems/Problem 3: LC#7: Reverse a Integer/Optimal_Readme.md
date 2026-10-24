# LeetCode 7: Reverse Integer

## Optimal Approach: Mathematical Reversal

In this approach, I reverse the integer digit by digit using modulo and integer division without converting the number into a string.

### Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
```

### Example

```python
Input:    120
Output:   21
Expected: 21
```

### Why it Works

In each iteration, the last digit is extracted using `% 10` and added to the reversed number. The original number is reduced using `// 10` until no digits remain. Finally, the sign and 32-bit integer constraints are handled.

### Complexity

- **Time Complexity: O(log n)** → The loop runs once for each digit in the number.
- **Space Complexity: O(1)** → Only constant extra variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| String Reversal | O(n) | O(n) |
| Mathematical Reversal | O(log n) | O(1) |

### Key Learning

- Reversing an integer mathematically is more efficient than using string conversion.
- The number of digits in an integer is `log₁₀(n)`, which gives the optimal time complexity of **O(log n)**.
- This is the preferred interview solution because it uses constant extra space.
