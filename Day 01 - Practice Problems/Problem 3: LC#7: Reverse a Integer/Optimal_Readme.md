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

        if rev < -2**31 or***v > 2**31 - 1:
            retur* 0

        return rev
```

### Ex*mple

```python
Input:    120
Outp*t:   21
Expected: 21
```

### Why *t Works

In each iteration, the la*t digit is extracted using `% 10` *nd added to the reversed number. T*e original number is reduced using*`// 10` until no digits remain. Fi*ally, the sign and 32-bit integer *onstraints are handled.

### Compl*xity

- **Time Complexity: O(log n*** → The loop runs once for each d*git in the number.
- **Space Compl*xity: O(1)** → Only constant extra*variables are used.

### Compariso*

| Approach | Time Complexity | S*ace Complexity |
|-----------|----*-----------|------------------|
| *tring Reversal | O(n) | O(n) |
| M*thematical Reversal | O(log n) | O*1) |

### Key Learning

- Reversin* an integer mathematically is more*efficient than using string conver*ion.
- The number of digits in an *nteger is `log₁₀(n)`, which gives the optimal time complexity of **O(log n)**.
- This is the preferred interview solution because it uses constant extra space.
