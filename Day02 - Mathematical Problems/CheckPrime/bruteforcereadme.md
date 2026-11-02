# Check Prime Number

## Approach 1: Brute Force

In this approach, I check whether the number is divisible by any number from `2` to `n-1`. If a divisor is found, the number is not prime.

### Code

```python
class Solution:
    def checkPrime(self, n: int) -> bool:
        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
```

### Example

```python
Input:    7
Output:   True
Expected: True
```

### Why it Works

A prime number has exactly two factors: `1` and itself. If any number between `2` and `n-1` divides `n`, then `n` is not prime.

### Complexity

- **Time Complexity: O(n)** → In the worst case, every number from `2` to `n-1` is checked.
- **Space Complexity: O(1)** → Only a few variables are used.

### Limitation

Many unnecessary checks are performed, making it inefficient for large numbers.
