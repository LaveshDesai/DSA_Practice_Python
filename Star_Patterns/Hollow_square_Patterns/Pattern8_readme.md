# Hollow Square Pattern

## Approach

In this pattern, stars are printed only on the boundary of the square.

A star is printed when the current position belongs to:

- The first row
- The last row
- The first column
- The last column

All remaining positions are filled with spaces, which creates the hollow area inside the square.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if i == 1 or j == 1 or i == n or j == n:
            print("*", end="")
        else*
            print(" ", end="")

 *  print()
```

### Example

Input: 5

Output:

```text
*****
*   *
*   *
*   *
*****
```

### Logic

- The outer loop controls the rows.
- The inner loop controls the columns.
- If the current position is on the boundary of the square, print `*`.
- Otherwise, print a space.

### Complexity

- **Time Complexity: O(n²)** → Every position in the `n × n` square is visited once.
- **Space Complexity: O(1)** → No extra space is used.

### Interview Follow-up

**Why do we check `i == 1` and `i == n`?**

→ These conditions identify the top and bottom borders of the square.

**Why do we check `j == 1` and `j == n`?**

→ These conditions identify the left and right borders of the square.

**What happens if we remove the `else` block?**

→ The pattern becomes a solid square because every position will contain a star.

### Key Learning

Many hollow patterns can be solved by identifying the boundary cells and printing symbols only for those positions.
