## Time Complexity Comparison

### Better Approach (Counting Method)

The counting approach works in two phases:

### Phase 1: Count Frequencies

```python
for i in range(n):
```

Time Complexity:

```text
O(n)
```

### Phase 2: Rewrite the Array

```python
while countZero > 0
while countOne > 0
while countTwo > 0
```

Together, these loops rewrite exactly `n` elements.

Time Complexity:

```text
O(n)
```

### Total Time Complexity

```text
O(n) + O(n)
= O(2n)
```

Using Big-O notation, constants are ignored:

```text
O(2n) = O(n)
```

---

### Optimal Approach (Dutch National Flag Algorithm)

The Dutch National Flag Algorithm uses three pointers:

```python
low
mid
high
```

and processes the array in a single traversal.

```python
while mid <= high:
```

Each element is examined at most once and moved to its correct position.

### Total Time Complexity

```text
O(n)
```

---

## Why Is the Optimal Approach Considered Better?

Although both approaches have an overall time complexity of:

```text
O(n)
```

the counting method requires **two traversals** of the array:

```text
1st Pass → Count frequencies
2nd Pass → Rewrite the array
```

Total work:

```text
O(2n)
```

The Dutch National Flag Algorithm performs the sorting during a **single traversal**:

```text
1 Pass → Sort while scanning
```

Total work:

```text
O(n)
```

Since it accomplishes the task in one pass without first counting frequencies, it is considered the optimal solution.

---

## Complexity Comparison

| Approach | Number of Passes | Time Complexity | Space Complexity |
|-----------|-----------------|----------------|------------------|
| Counting Method | 2 | O(2n) ≈ O(n) | O(1) |
| Dutch National Flag Algorithm | 1 | O(n) | O(1) |

---

## Interview Answer

Both the counting approach and the Dutch National Flag Algorithm have an overall time complexity of **O(n)** and a space complexity of **O(1)**. However, the counting approach requires two traversals of the array, resulting in **O(2n)** operations, while the Dutch National Flag Algorithm sorts the array in a single traversal with **O(n)** operations. Therefore, the Dutch National Flag Algorithm is considered the optimal solution.
