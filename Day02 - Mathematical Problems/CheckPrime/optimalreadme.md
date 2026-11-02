# Check Prime Number

## Optimal Approach: Check Until √n

In this approach, I only check divisors up to the square root of the number.

### Code

```python
class Solution:
    def checkPrime(self, n: int) -> bool:
        if n <= 1:
            return False

        i = 2

        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True
```

### Example

```python
Input:    7
Output:   True
Expected: True
```

### Why it Works

If a number has a factor greater than √n, it must also have a factor smaller than √n. Therefore, checking beyond √n is unnecessary.

### Complexity

- **Time Complexity: O(√n)** → Only numbers from `2` to `√n` are checked.
- **Space Complexity: O(1)** → Only a few variables are used.

### Interview Follow-up Questions

**1. Why do we check only till √n?**  
→ Every factor above √n has a corresponding factor below √n.

**2. Why is 1 not a prime number?**  
→ A prime number must have exactly two factors, but 1 has only one factor.

**3. Why use `i * i <= n` instead of `i <= sqrt(n)`?**  
→ It avoids calculating square roots repeatedly and is more efficient.

**4. Why return False when `n <= 1`?**  
→ Negative numbers, 0, and 1 are not prime numbers.

### Key Learning

- Prime numbers have exactly two factors.
- Checking until √n reduces unnecessary operations.
- This is the standard interview-optimal solution.
