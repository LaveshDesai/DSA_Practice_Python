# Concentric Number Pattern

## Approach

In this pattern, the numbers are arranged in concentric layers.

For every position `(i, j)`:

- Find the minimum distance from the top, bottom, left, and right boundaries.
- Subtract that distance from `n`.
- The resulting value is printed at that position.

This creates a square pattern with decreasing numbers as we move towards the center.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(2 * n - 1):
    for j in range(2 * n - 1):

        top = i
        left = j
        right = (2 * n - 2) - j
        down = (2 * n - 2) - i

        print(n - min(min(top, down), min(left, right)), end=" ")

    print()
```

### Example

Input:

```text
4
```

Output:

```text
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```

### Logic

- `top` stores the distance from the top boundary.
- `left` stores the distance from the left boundary.
- `right` stores the distance from the right boundary.
- `down` stores the distance from the bottom boundary.
- The minimum of these four distances determines the current layer.
- Subtracting the layer value from `n` gives the number to print.

### Complexity

- **Time Complexity: O(n²)** → A `(2n - 1) × (2n - 1)` grid is traversed once.
- **Space Complexity: O(1)** → No extra data structure is used.

### Interview Follow-up

**Why do we take the minimum of the four distances?**

→ The minimum distance determines how close the current position is to the nearest boundary.

**Why is the grid size `(2 * n - 1)`?**

→ It provides enough rows and columns to form all concentric layers from `n` to `1`.

**Can this pattern be solved without storing the four distances?**

→ Yes, but using the four distances makes the logic easier to understand and implement.

### Key Learning

Many pattern problems become easier when treated as coordinate-based problems. Instead of thinking row by row, focus on the position of each cell and its distance from the boundaries.
