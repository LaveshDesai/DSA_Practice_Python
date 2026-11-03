# 🦋 Butterfly Pattern in Python (Single Outer Loop)

## Approach

This approach prints the complete butterfly pattern using **one outer `for` loop** instead of writing separate outer loops for the increasing and decreasing halves.

We introduce variables (`stars` and `space`) to dynamically control the pattern for each row.

### Why Use Variables?

- `stars = i`: Controls the number of stars in the increasing half.
- `space = 2 * n - 2 * i`: Calculates the middle spaces.
- `if i > n`: Updates the variables to reverse the pattern for the decreasing half.

By updating these variables, we can print both halves using a single outer loop without needing a second outer loop.

## Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, 2 * n):
    stars = i
    space = 2 * n - 2 * i

    if i > n:
        stars = 2 * n - i
        space = 2 * i - 2 * n

    for j in range(1, stars + 1):
        print("*", end="")

    for j in range(1, space + 1):
        print(" ", end="")

    for j in range(1, stars + 1):
        print("*", end="")

    print()
```

## Example

**Input:**
```text
5
```

**Output:**
```text
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

## Logic Explanation

For `n = 5`, the outer loop runs from `1` to `9` (`2 * n - 1` rows).

| Row (i) | Stars | Spaces | Condition |
|---|---:|---:|---|
| 1 | 1 | 8 | Increasing |
| 2 | 2 | 6 | Increasing |
| 3 | 3 | 4 | Increasing |
| 4 | 4 | 2 | Increasing |
| 5 | 5 | 0 | Middle |
| 6 | 4 | 2 | Decreasing |
| 7 | 3 | 4 | Decreasing |
| 8 | 2 | 6 | Decreasing |
| 9 | 1 | 8 | Decreasing |

### How Variables Work

**1. Increasing Half (`i <= n`)**

- `stars = i`
- `space = 2 * (n - i)`

As the row number increases, stars increase and spaces decrease.

**2. Decreasing Half (`i > n`)**

- `stars = 2 * n - i`
- `space = 2 * i - 2 * n`

The variables reverse their values, decreasing the stars and increasing the spaces.

### Why Does This Eliminate the Second Outer Loop?

Normally, we use two separate outer loops:
- First loop prints the increasing half.
- Second loop prints the decreasing half.

Here, `range(1, 2 * n)` handles all rows in one loop. The `if` condition changes the values of `stars` and `space` after the middle row.

Therefore, we eliminate the need for a second outer loop while keeping the nested loops responsible for printing stars and spaces.

## Complexity Analysis

- **Time Complexity: O(n²)** – The outer loop runs `2n - 1` times, and the inner loops perform up to O(n) printing operations per row.
- **Auxiliary Space Complexity: O(1)** – Only variables are used; no additional data structures are required.

## Key Learning

- Using a single outer loop for both increasing and decreasing patterns.
- Introducing variables to control stars and spaces dynamically.
- Using conditional statements to change pattern behaviour.
- Reducing duplicate loop logic through variable manipulation.
