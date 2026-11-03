# Star Pattern (Single Loop Solution)

## Approach

In the previous solution, I used two outer loops:

- The first loop printed the increasing pattern.
- The second loop printed the decreasing pattern.

In this solution, I use only one outer loop to generate the same pattern. Once the pattern reaches `n` stars, I adjust the value of `i` so that the number of stars starts decreasing.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, 2 * n):
    if i > n:
        i = 2 * n - i

    for j in range(i):
        print("*", end="")

    print()
```

### Example

Input:

```text
5
```

Output:

```text
*
**
***
****
*****
****
***
**
*
```

### Logic

- The loop runs from `1` to `2*n - 1`.
- For values from `1` to `n`, the number of stars increases.
- After reaching `n`, the value of `i` is changed using:

```python
i = 2 * n - i
```

- This makes the number of stars decrease from `n-1` back to `1`.

### Complexity

- **Time Complexity: O(n²)** → The total number of stars printed is `1 + 2 + 3 + ... + n + (n-1) + ... + 1`.
- **Space Complexity: O(1)** → No extra space is used.

### Comparison with Previous Approach

| Approach | Outer Loops | Time Complexity | Space Complexity |
|----------|------------|----------------|------------------|
| Two Loop Solution | 2 | O(n²) | O(1) |
| Single Loop Solution | 1 | O(n²) | O(1) |

### Advantage

- Uses only one outer loop.
- Requires fewer lines of code.
- Produces the same output as the previous solution.

### Interview Follow-up

**Why do we use `i = 2 * n - i`?**

→ It changes the increasing count into a decreasing count after reaching the middle row.

### Key Learning

The same pattern can be solved in multiple ways. Using a single outer loop makes the solution shorter while keeping the same time and space complexity.
