# Union of Two Sorted Arrays

## Optimal Approach: Two Pointers

Since both arrays are already sorted, I use two pointers to traverse them simultaneously.

- `i` points to the first array.
- `j` points to the second array.
- The smaller element is added to the union array.
- Duplicate values are skipped by comparing with the last inserted element.
- If one array gets exhausted, the remaining elements of the other array are added.

This allows us to utilize the sorted order of the arrays and avoid using a set.

### Code

```python
def sortedArray(a: [int], b: [int]) -> [int]:

    union = []

    n1 = len(a)
    n2 = len(b)

    i = 0
    j = 0

    while i < n1 and j < n2:

        if a[i] <= b[j]:

            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])

            i += 1

        else:

            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])

            j += 1

    while i < n1:

        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])

        i += 1

    while j < n2:

        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])

        j += 1

    return union
```

### Example

Input:

```python
a = [1, 1, 2, 3, 4]
b = [2, 2, 3, 5]
```

Output:

```python
[1, 2, 3, 4, 5]
```

### Logic

- Start with two pointers at the beginning of both arrays.
- Compare the current elements.
- Insert the smaller element into the union array if it is not already present.
- Move the corresponding pointer forward.
- After one array is fully traversed, add the remaining unique elements from the other array.

### Why It Works

Because both arrays are sorted:

- Smaller values appear before larger values.
- We can merge both arrays in a single traversal.
- Duplicate values can be skipped by checking the last element added to the union array.

### Complexity

- **Time Complexity: O(n1 + n2)** → Each element from both arrays is visited at most once.
- **Space Complexity: O(n1 + n2)** → In the worst case, all elements are unique and must be stored in the union array.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Set Approach | O((n1+n2) log(n1+n2)) | O(n1+n2) |
| Two Pointers (Optimal) | O(n1+n2) | O(n1+n2) |

### Improvement Over Set Approach

- No sorting is required after collecting elements.
- Makes use of the fact that the arrays are already sorted.
- Reduces the time complexity from **O((n1+n2) log(n1+n2))** to **O(n1+n2)**.

### Interview Follow-up

**Why do we use two pointers?**

→ Since both arrays are sorted, two pointers allow us to process them efficiently in a single traversal.

**Why do we check `union[-1] != current_element`?**

→ To avoid inserting duplicate values into the union array.

**Why are the last two `while` loops needed?**

→ One array may finish before the other, so the remaining unique elements must still be added.

### Key Learning

Whenever two sorted arrays need to be merged or compared, the Two Pointers technique is often the most efficient approach because it processes both arrays in linear time.
