# Diamond Star Pattern

## Approach: Pyramid + Inverted Pyramid

In this approach, I first print the upper pyramid and then print the lower inverted pyramid. The middle row is printed only once.

### Code

```python
n = int(input("Enter the value of n: "))

# Upper Half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower Half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
```

### Example

```python
Input: 5
```

Output:

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

### Why it Works

- `n - i` prints the leading spaces.
- `2 * i - 1` prints odd numbers of stars.
- The first loop creates the upper pyramid.
- The second loop creates the lower pyramid.
- Starting the second loop from `n - 1` avoids printing the middle row twice.

### Complexity

- **Time Complexity: O(n²)** → Nested loops print spaces and stars for each row.
- **Space Complexity: O(1)** → No extra data structure is used.

### Interview Follow-up Questions

**1. Why is `(2 * i - 1)` used?**  
→ It generates odd numbers of stars (1, 3, 5, 7, ...), which keeps the pattern symmetric.

**2. Why is `(n - i)` used?**  
→ It creates the leading spaces needed to center the stars.

**3. Why start the second loop from `n - 1`?**  
→ To avoid printing the middle row twice.

### Key Learning

- Diamond patterns are formed by combining a pyramid and an inverted pyramid.
- Most pattern problems can be solved by controlling rows, spaces, and symbols separately.
