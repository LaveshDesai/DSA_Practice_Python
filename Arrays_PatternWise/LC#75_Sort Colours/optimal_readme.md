# Sort Colors - Optimal Approach (Dutch National Flag Algorithm)

## Problem Statement

Given an array containing only:

```text
0 → Red
1 → White
2 → Blue
```

Sort the array in-place so that all `0`s come first, followed by all `1`s, and then all `2`s.

You must modify the array without using extra space.

---

## Intuition

Since the array contains only three distinct values (`0`, `1`, and `2`), we can divide the array into three regions:

```text
0s Region | Unknown Region | 2s Region
```

Three pointers are used:

```python
low
mid
high
```

- `low` tracks the position for the next `0`.
- `mid` scans the array.
- `high` tracks the position for the next `2`.

This approach is known as the **Dutch National Flag Algorithm**.

---

## Algorithm

### If `arr[mid] == 0`

Swap `low` and `mid`.

```python
arr[mid], arr[low] = arr[low], arr[mid]
```

Move:

```python
low += 1
mid += 1
```

---

### If `arr[mid] == 1`

`1` is already in its correct region.

Move:

```python
mid += 1
```

---

### If `arr[mid] == 2`

Swap `mid` and `high`.

```python
arr[mid], arr[high] = arr[high], arr[mid]
```

Move:

```python
high -= 1
```

Do not move `mid` because the newly swapped element must still be processed.

---

## Code

```python
def sortArray(arr, n):

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
```

---

## Example

### Input

```python
arr = [2, 0, 2, 1, 1, 0]
```

### Output

```python
[0, 0, 1, 1, 2, 2]
```

---

## Time Complexity

```text
O(n)
```

### Reason

Each element is visited at most once by the `mid` pointer.

---

## Space Complexity

```text
O(1)
```

### Reason

Only three variables (`low`, `mid`, and `high`) are used. No extra array or data structure is required.

---

## Why Is This Optimal?

The counting approach requires two passes:

1. Count frequencies.
2. Rewrite the array.

The Dutch National Flag Algorithm sorts the array in a single traversal while maintaining O(1) extra space, making it the optimal solution.

---

## Interview Answer

The Dutch National Flag Algorithm uses three pointers (`low`, `mid`, and `high`) to partition the array into regions of `0`s, `1`s, and `2`s. Each element is processed only once, resulting in **O(n)** time complexity and **O(1)** extra space complexity. Since it sorts the array in a single traversal without using additional data structures, it is considered the optimal solution for LeetCode 75.
