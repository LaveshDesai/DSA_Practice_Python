# Second Largest Element in an Array

## Optimal Approach: Single Traversal

In this approach, I find the largest and second largest elements in a single traversal of the array.

I maintain two variables:

- `largest` stores the largest element found so far.
- `secondLargest` stores the second largest distinct element found so far.

Whenever a larger element is found, the current largest becomes the second largest.

### Code

```python
class Solution:

    def getSecondOrderElements(self, a: list[int]) -> int:

        n = len(a)

        largest = a[0]
        secondLargest = -1

        for i in range(n):

            if a[i] > largest:
                secondLargest = largest
                largest = a[i]

            elif a[i] < largest and a[i] > secondLargest:
                secondLargest = a[i]

        return secondLargest
```

### Example

Input:

```python
a = [1, 3, 4, 2, 8, 8, 6]
```

Output:

```python
6
```

### Logic

- Assume the first element is the largest.
- Traverse the array once.
- If a larger element is found:
  - Move the current largest to secondLargest.
  - Update largest.
- Otherwise, if the current element is smaller than largest but larger than secondLargest:
  - Update secondLargest.
- At the end of the traversal, secondLargest contains the second largest distinct element.

### Why It Works

Whenever a new maximum element is found, the previous maximum automatically becomes a candidate for the second largest element.

This allows both values to be maintained in a single pass without sorting.

### Complexity

- **Time Complexity: O(n)** → The array is traversed exactly once.
- **Space Complexity: O(1)** → Only two variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Two Pass Traversal | O(n) | O(1) |
| Single Traversal (Optimal) | O(n) | O(1) |

### Improvement Over Previous Approach

- No sorting is required.
- No second traversal is required.
- Largest and second largest elements are found together in one pass.

### Interview Follow-up

**Why do we update `secondLargest` before updating `largest`?**

→ When a new largest element is found, the previous largest becomes the second largest candidate.

**Why do we check `a[i] < largest` in the `elif` condition?**

→ This prevents duplicate occurrences of the largest element from being considered as the second largest.

**Can this approach handle duplicate maximum values?**

→ Yes. Duplicate largest values are ignored because the second largest must be a distinct element.

### Key Learning

When multiple values need to be tracked during a traversal, maintaining separate variables often eliminates the need for sorting or multiple passes through the array.
