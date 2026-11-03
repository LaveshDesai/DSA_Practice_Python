# Butterfly Pattern

## Approach

In this pattern, the first half prints an inverted butterfly and the second half prints a normal butterfly.

For each row:

- First, print stars on the left side.
- Then, print spaces in the middle.
- Finally, print stars on the right side.

The number of stars decreases in the first half and increases in the second half.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")

    for j in r*nge*2 * (n - i)):
       *print(" ", end="")

    for j in*range(i, 0, -1):
       *print("*", end="")

    print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="*)

    for j in range(2 * (* - i)):
        print(" ", end="*)

    for j in range(1, i + 1*:
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
**********
****  ****
***    ***
**      **
*       **
*        *
**      **
***    ***
****  ****
**********
```

### Logic

- The first outer loop prints the upper half of the butterfly.
- The second outer loop prints the lower half of the butterfly.
- `i` controls the number of stars printed on both sides.
- `2 * (n - i)` controls the gap between the stars.
- As the number of stars decreases, the gap increases.
- As the number of stars increases, the gap decreases.

### Complexity

- **Time Complexity: O(n²)** → Nested loops are used to print stars and spaces for every row.
- **Space Complexity: O(1)** → No extra space is used.

### Interview Follow-up

**Why do we use `2 * (n - i)` spaces?**

→ The gap must increase by 2 spaces in every row to maintain the butterfly shape.

**Why are there two outer loops?**

→ One loop prints the upper half and the other prints the lower half of the butterfly.

### Key Learning

This pattern is formed by combining two mirrored star patterns with a variable gap between them.

