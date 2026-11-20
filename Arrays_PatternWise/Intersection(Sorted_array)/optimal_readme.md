# Intersection of Two Sorted Arrays

## Optimal Approach: Two Pointers

Since both arrays are already sorted, I use two pointers to traverse them simultaneously.

- `i` points to the first array.
- `j` points to the second array.
- If the elements are equal, they belong to the intersection.
- If one element is smaller, move its pointer forward.
- Continue until one of the arrays is fully traversed.

This approach takes advantage of the sorted nature of the arrays and avoids unnecessary comparisons.

### Code

```python
def findArrayIntersection(arr: list, n: int, brr: list, m: int):

    result = []

    i, j = 0, 0

    while i < n and j < m:

        if arr[i] < brr[j]:
            i += 1

        elif brr[j] < arr[i]:
            j += 1

        else:
            result.append(arr[i])
            i += 1
            j += 1

    return result
```

### Example

Input:

```python
arr = [1, 2, 2, 3, 4]
brr = [2, 2, 3, 5]
```

Output:

```python
[2, 2, 3]
```

### Logic

- Start with pointers at the beginning of both arrays.
- Compare the current elements.
- If the element in the first array is smaller, move `i`.
- If the element in the second array is smaller, move `j`.
- If both elements are equal:
  - Add the element to the result.
  - Move both pointers forward.
- Continue until one of the arrays is exhausted.

### Why It Works

Because both arrays are sorted:

- Elements smaller than the current element in the other array cannot be part of the future intersection.
- Therefore, we can safely move the pointer of the smaller element.
- This allows us to process both arrays in a single traversal.

### Complexity

- **Time Complexity: O(n + m)** → Each element is visited at most once.
- **Space Complexity: O(k)** → `k` is the number of common elements stored in the result array.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force + Visited Array | O(n × m) | O(m) |
| Two Pointers (Optimal) | O(n + m) | O(k) |

### Improvement Over Brute Force

- No nested loops are required.
- No visited array is needed.
- Makes use of the sorted order of the arrays.
- Reduces the time complexity from **O(n × m)** to **O(n + m)**.

### Interview Follow-up

**Why does the Two Pointers approach work?**

→ Because both arrays are sorted, we can decide which pointer to move based on the smaller element.

**Why do we move both pointers when a match is found?**

→ The matching element has already been added to the intersection, so both pointers can move to the next values.

**Can this approach work for unsorted arrays?**

→ No. The arrays must be sorted. For unsorted arrays, we would typically use a hash set or sorting first.

### Key Learning

Whenever two sorted arrays need to be compared, merged, or intersected, the Two Pointers technique is often the most efficient solution because it processes both arrays in linear time.
