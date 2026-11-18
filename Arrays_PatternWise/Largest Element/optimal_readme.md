# Largest Element in an Array

## Optimal Approach: Linear Traversal

In this approach, I traverse the array once and keep track of the largest element seen so far.

For every element:

- Compare it with the current largest value.
- Update the largest value if a bigger element is found.

At the end of the traversal, the largest variable stores the maximum element in the array.

### Code

```python
class Solution:
    def linearSearch(self, nums: list[int]) -> int:

        n = len(nums)
        largest = nums[0]

        for i in range(1, n):
            largest = max(largest, nums[i])

        return largest
```

### Example

Input:

```python
nums = [5, 4, 1, 9, 2]
```

Output:

```python
9
```

### Logic

- Assume the first element is the largest.
- Traverse the remaining elements.
- Compare each element with the current largest value.
- Update the largest value whenever a larger element is found.
- Return the largest element after the traversal is complete.

### Why It Works

The largest element must appear somewhere in the array.

By comparing every element with the current largest value, we guarantee that the final value stored in `largest` will be the maximum element in the array.

### Complexity

- **Time Complexity: O(n)** → The array is traversed exactly once.
- **Space Complexity: O(1)** → Only one extra variable (`largest`) is used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Linear Traversal (Optimal) | O(n) | O(1) |

### Improvement Over Sorting

- Sorting the entire array is unnecessary when we only need the largest element.
- A single traversal is enough to find the answer.
- Reduces the time complexity from **O(n log n)** to **O(n)**.

### Interview Follow-up

**Why do we initialize `largest` with `nums[0]`?**

→ We need a valid starting value for comparison, so the first element is assumed to be the largest initially.

**Why can't we initialize `largest` as `0`?**

→ The array may contain negative numbers, which could lead to incorrect results.

**Can we solve this using sorting?**

→ Yes, but sorting performs extra work because we only need the maximum element, not the entire sorted array.

### Key Learning

When only the maximum or minimum value is required, a single traversal is usually more efficient than sorting the entire array.
