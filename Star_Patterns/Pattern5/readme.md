# Floyd's Triangle Pattern

## Approach

In this pattern, numbers are printed continuously in increasing order.

I use a variable `num` to keep track of the current number. After printing a number, I increment it by `1` so that the next number is printed in sequence.

### Code

```python
n = int(input("Enter the value of n:"))

num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num + 1

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
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

### Logic

- `num` stores the current number to be printed.
- The outer loop controls the rows.
- The inner loop prints values in the current row.
- After printing a number, `num` is incremented so the sequence continues in the next position.

### Complexity

- **Time Complexity: O(n²)** → A total of `1 + 2 + 3 + ... + n` numbers are printed.
- **Space Complexity: O(1)** → Only the variable `num` is used.

### Interview Follow-up

**Why do we use a separate variable `num`?**

→ It helps maintain a continuous sequence across all rows.

**What happens if we print `j` instead of `num`?**

→ The numbers would restart from `1` in every row instead of continuing the sequence.

### Key Learning

This pattern shows how a single variable can be carried across multiple rows to generate a continuous sequence of numbers.
