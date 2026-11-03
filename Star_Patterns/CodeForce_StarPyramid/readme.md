# ⭐ Star Triangle Pattern in Python

## Approach

The Star Triangle pattern is printed using nested `for` loops.

Each row contains:
- **Spaces:** Decrease by 1 in every row.
- **Stars:** Increase by 2 in every row.

We use two inner loops to control the spaces and stars.

## Code

```python
def nStarTriangle(n: int) -> None:
    for i in range(n):
        # Spaces
        for j in range(n - i - 1):
            print(" ", end="")

        # Stars
        for j in range(2 * i + 1):
            print("*", end="")

        print()
```

## Example

**Input:**
```text
4
```

**Output:**
```text
   *
  ***
 *****
*******
```

## Logic Explanation

- `range(n)` controls the number of rows.
- `n - i - 1` calculates the spaces before the stars.
- `2 * i + 1` calculates the number of stars in each row.
- `end=""` prints spaces and stars on the same line.
- `print()` moves to the next row.

### Row-wise Breakdown (n = 4)

| Row (`i`) | Spaces | Stars |
|---|---:|---:|
| 0 | 3 | 1 |
| 1 | 2 | 3 |
| 2 | 1 | 5 |
| 3 | 0 | 7 |

## Complexity Analysis

- **Time Complexity: O(n²)** – Nested loops print spaces and stars for each row.
- **Auxiliary Space Complexity: O(1)** – No extra data structures are used.

## Key Learning

Nested Loops | Pattern Printing | Space Calculation | Star Calculation | Time & Space Complexity
