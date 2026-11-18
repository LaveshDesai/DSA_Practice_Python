# Largest Element in an Array

## Approach 1: Sorting

In this approach, I sort the array in ascending order and return the last element because the last element of a sorted array is always the largest.

### Code

```python
def largestElement(arr: [], n: int) -> int:

    arr.sort()

    return arr[n - 1]
```

### Example

Input:

```python
arr = [5, 4, 1, 9, 2]
```

Output:

```python
9
```

### Logic

- Sort the array in ascending order.
- After sorting, the largest element will be present at the last index.
- Return the element at index `n - 1`.

### Complexity

- **Time Complexity: O(n log n)** → Python's `sort()` uses Timsort, which takes O(n log n) time in the average and worst case.
- **Space Complexity: O(1)** → No extra data structure is explicitly used.

### Limitation

Sorting the entire array is unnecessary because we only need the largest element, not the sorted order of all elements.

### Interview Follow-up

**Why is the last element the largest after sorting?**

→ Sorting arranges the elements in ascending order, so the largest element naturally moves to the last position.

**Can we find the largest element without sorting?**

→ Yes. We can traverse the array once and keep track of the maximum element seen so far.

### Key Learning

Although sorting solves the problem, it performs extra work. If we only need the largest element, a single traversal is a more efficient approach.
