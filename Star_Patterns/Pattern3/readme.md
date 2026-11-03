# Binary Number Triangle Pattern

## Approach

In this pattern, each row starts with either `1` or `0` depending on whether the row number is odd or even.

- Odd rows start with `1`.
- Even rows start with `0`.
- After printing a number, I switch it using:

```python
start = 1 - start
```

This helps alternate between `0` and `1` in the same row.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1, n + 1):

    if i % 2 == 0:
        start = 0
    else:
        start = 1

    for j in range(i):
        print(start, end=" ")
        start = 1 - start

    print()
```

### Example

Input:

```text
5
```

Output:

```text
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

### Logic

- If the row number is odd, start with `1`.
- If the row number is even, start with `0`.
- After every print, switch the value using `1 - start`.
- The inner loop prints exactly `i` numbers in each row.

### Complexity

- **Time Complexity: O(n²)** → Total elements printed are `1 + 2 + 3 + ... + n`.
- **Space Complexity: O(1)** → Only a few variables are used.

### Interview Follow-up

**Why do we use `start = 1 - start`?**

→ It toggles the value between `0` and `1`.

**Why do odd rows start with `1` and even rows start with `0`?**

→ This follows the pattern requirement and creates the alternating binary structure.

### Key Learning

This pattern demonstrates how a value can be toggled efficiently without using extra conditions inside the inner loop.
