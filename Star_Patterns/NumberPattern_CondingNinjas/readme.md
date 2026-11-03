# Number Triangle Pattern

## Approach

In this pattern, each row starts with the row number and prints consecutive numbers.

For example:

- Row 1 starts with `1`
- Row 2 starts with `2`
- Row 3 starts with `3`
- Row 4 starts with `4`

The number of elements printed in each row is equal to the row number.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    for j in range(i, 2 * i):
        print(j, end="")

    print()
```

### Example

Input:

```text
4
```

Output:

```text
1
23
345
4567
```

### Logic

- The outer loop controls the rows.
- The inner loop starts from `i` and goes up to `2 * i - 1`.
- This prints consecutive numbers starting from the current row number.
- The number of values printed in each row is equal to the row number.

### Complexity

- **Time Complexity: O(n²)** → The total numbers printed are `1 + 2 + 3 + ... + n`.
- **Space Complexity: O(1)** → No extra space is used.

### Interview Follow-up

**Why does the inner loop run from `i` to `2 * i`?**

→ It prints exactly `i` consecutive numbers starting from `i`.

**Why is the upper limit `2 * i` not included?**

→ Python's `range()` excludes the ending value, so the last number printed is `2 * i - 1`.

### Key Learning

This pattern shows how changing the starting value of the inner loop can generate different number sequences in each row.
