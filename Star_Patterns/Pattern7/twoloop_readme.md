# 🦋 Butterfly Pattern in Python

## Approach

The butterfly pattern consists of two halves:

1. **Upper Half:** Stars increase and middle spaces decrease.
2. **Lower Half:** Stars decrease and middle spaces increase.

Each row contains left-side stars, middle spaces, and right-side stars.

## Code

    n = int(input("Enter the value of n: "))

    # Upper Half
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

    # Lower Half
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

## Example

**Input:**

    5

**Output:**

    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *

## Logic

- `i` controls the number of stars on both sides.
- `2 * (n - i)` controls the middle spaces.
- The second outer loop starts from `n - 1` to avoid repeating the middle row.

## Complexity

- **Time Complexity:** O(n²) – Nested loops print stars and spaces.
- **Auxiliary Space Complexity:** O(1) – No extra data structures are used.

## Key Learning

Nested Loops | Pattern Printing | Increasing & Decreasing Patterns | Time & Space Complexity
