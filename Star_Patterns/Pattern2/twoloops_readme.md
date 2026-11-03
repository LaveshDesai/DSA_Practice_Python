# Star Pattern

## Approach

I used two loops:

- The first loop prints stars from `1` to `n`.
- The second loop prints stars from `n-1` to `1`.

By combining both parts, the required pattern is formed.

### Code

```python
n = int(input("Enter the value of n:"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end="")
    print()
```

### Example

Input:

```text
5
```

Output:

```text
*
**
***
****
*****
****
***
**
*
```

### Logic

- `i` represents the current row.
- The first outer loop increases the number of stars in each row.
- The second outer loop decreases the number of stars in each row.

### Complexity

- **Time Complexity: O(n²)** → Total stars printed = `1 + 2 + 3 + ... + n + (n-1) + ... + 1`.
- **Space Complexity: O(1)** → No extra space is used.

### Interview Follow-up

**Why does the second loop start from `n-1`?**

→ To avoid printing the middle row twice.

### Key Learning

This pattern is created by combining an increasing star triangle and a decreasing star triangle.
