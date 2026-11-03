# Number Crown Pattern

## Approach

In this pattern:

- The first part prints numbers from `1` to `i`.
- The middle part prints spaces.
- The last part prints numbers from `i` back to `1`.

As the row number increases:
- The number sequence grows.
- The gap in the middle decreases.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
```

### Example

Input:

```text
5
```

Output:

```text
1        1
12      21
123    321
1234  4321
1234554321
```

### Logic

- The first loop prints numbers in increasing order.
- The second loop prints the spaces between the two number sequences.
- The third loop prints numbers in decreasing order.
- As `i` increases, the number of spaces decreases and the pattern closes toward the center.

### Complexity

- **Time Complexity: O(n²)** → Each row prints numbers and spaces using nested loops.
- **Space Complexity: O(1)** → No extra data structure is used.

### Interview Follow-up

**Why do we print `2 * (n - i)` spaces?**

→ The space gap decreases by 2 in every row to maintain symmetry.

**Why does the last loop run from `i` to `1`?**

→ It creates the mirror image of the increasing sequence.

### Key Learning

This pattern is built using three parts in every row:

1. Increasing numbers
2. Spaces
3. Decreasing numbers

Combining these three sections creates a symmetric number pattern.
