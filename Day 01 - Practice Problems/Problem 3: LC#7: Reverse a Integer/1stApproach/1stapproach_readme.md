# LeetCode 7: Reverse Integer

## Approach 1: Convert Integer to String

In this approach, I convert the integer into a string, reverse the string using slicing, and then convert it back to an integer.

### Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        x = str(abs(x))
        rev = int(x[::-1]) * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
```

### Example

```python
Input:    123
Output:   321
Expected: 321
```

### Why it Works

The number is converted to a string, reversed using slicing (`[::-1]`), converted back to an integer, and the original sign is restored. Finally, the 32-bit integer limit is checked.

### Complexity

- **Time Complexity: O(n)** → Reversing the string requires traversing all digits once.
- **Space Complexity: O(n)** → Extra space is used to store the reversed string.

### Limitation

This approach uses string conversion, which is usually not preferred in interviews when the problem can be solved mathematically.
