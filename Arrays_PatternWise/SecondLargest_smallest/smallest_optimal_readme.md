# Second Smallest Element in an Array

## Optimal Approach: Single Traversal

In this approach, I find the smallest and second smallest elements in a single traversal of the array.

I maintain two variables:

- `smallest` stores the smallest element found so far.
- `secondSmallest` stores the second smallest distinct element found so far.

Whenever a smaller element is found, the current smallest becomes the second smallest.

### Code

```python
class Solution:

    def getSecondOrderElements(self, a: list[int]) -> int:

        n = len(a)

        smallest = a[0]
        secondSmallest = float('inf')

        for i in range(1, n):

            if a[i] < smallest:
                secondSmallest = smallest
                smallest = a[i]

            elif a[i] != smallest and a[i] < secondSmallest:
                secondSmallest = a[i]

        return secondSmallest
```

### Example

Input:

```python
a = [1, 3, 4, 2, 8, 8, 6]
```

Output:

```python
2
```

### Logic

- Assume the first element is the smallest.
- Traverse the array once.
- If a smaller element is found:
  - Move the current smallest to `secondSmallest`.
  - Update `smallest`.
- Otherwise, if the current element is greater than `smallest` but smaller than `secondSmallest`:
  - Update `secondSmallest`.
- At the end of the traversal, `secondSmallest` contains the second smallest distinct element.

### Why It Works

Whenever a new minimum element is found, the previous minimum automatically becomes a candidate for the second smallest element.

This allows both values to be tracked in a single pass without sorting the array.

### Why Use `float('inf')`?

```python
secondSmallest = float('inf')
```

This ensures that any valid array element will be smaller than the initial value.

Example:

```python
a = [5, 8, 10]
```

The first valid candidate for the second smallest element can easily replace `float('inf')`.

### Complexity

- **Time Complexity: O(n)** → The array is traversed exactly once.
- **Space Complexity: O(1)** → Only two variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Two Pass Traversal | O(n) | O(1) |
| Single Traversal (Optimal) | O(n) | O(1) |

### Improvement Over Previous Approaches

- No sorting is required.
- No second traversal is required.
- Smallest and second smallest elements are found together in a single pass.

### Interview Follow-up

**Why do we update `secondSmallest` before updating `smallest`?**

→ When a new smallest element is found, the previous smallest becomes the second smallest candidate.

**Why do we check `a[i] != smallest`?**

→ Duplicate occurrences of the smallest element should not be considered the second smallest element.

**Can this approach handle duplicate minimum values?**

→ Yes. Duplicate smallest values are ignored because the second smallest element must be distinct.

### Key Learning

When multiple values need to be tracked during traversal, maintaining separate variables often eliminates the need for sorting or multiple passes through the array.
