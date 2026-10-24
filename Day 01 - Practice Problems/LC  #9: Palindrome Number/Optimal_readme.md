# LeetCode 9: Palindrome Number

## Optimal Approach: Reverse Half of the Number

In this approach, I reverse only half of the number and compare it with the remaining half.

### Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0

        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10
```

### Example

```python
Input:    121
Output:   True
Expected: True
```

### Why it Works

I reverse only half of the digits instead of the entire number. For even-length numbers, both halves should be equal. For odd-length numbers, the middle digit is ignored using `rev // 10`.

### Complexity

- **Time Complexity: O(log n)** → The loop runs once for each digit (actually only half the digits).
- **Space Complexity: O(1)** → Only a few variables are used.

### Key Learning

- Negative numbers are never palindromes.
- Numbers ending in `0` cannot be palindromes unless the number is `0`.
- Reversing only half the number is the most efficient solution.
