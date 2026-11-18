# Second Largest Element in an Array

## Approach 1: Sorting (Brute Force)

In this approach, I first sort the array in ascending order. After sorting, the largest element will be at the last index.

Then, I traverse the array from right to left and find the first element that is different from the largest element. That element becomes the second largest distinct element.

### Code

```python
class Solution:
    def secondLargest(self, nums: list[int]) -> int:

        n = len(nums)

        nums.sort()

        largest = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] != largest:
                return nums[i]
```

### Example

Input:

```python
nums = [1, 8, 8, 8]
```

Output:

```python
1
```

### Logic

- Sort the array.
- Store the largest element.
- Traverse from the second last element towards the beginning.
- Find the first element that is different from the largest element.
- Return that element as the second largest.

### Why It Works

After sorting:

```python
[1, 8, 8, 8]
```

The largest element is:

```python
8
```

Starting from the right side, all `8`s are skipped. The first different element encountered is:

```python
1
```

which is the second largest distinct element.

### Complexity

- **Time Complexity: O(n log n)** → Sorting the array dominates the overall complexity.
- **Space Complexity: O(1)** → No extra data structure is used.

### Limitation

Sorting the entire array is unnecessary because we only need the largest and second largest elements.

### Interview Follow-up

**Why do we start traversing from `n - 2`?**

→ The last element is already the largest after sorting.

**Why do we check `nums[i] != largest`?**

→ Duplicate occurrences of the largest element should not be considered the second largest element.

**Can we solve this without sorting?**

→ Yes. We can find the largest and second largest elements in a single traversal using two variables.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting (Current) | O(n log n) | O(1) |
| Linear Traversal (Optimal) | O(n) | O(1) |

### Key Learning

Sorting is a simple way to find the second largest element, but it performs extra work. A single traversal can solve the problem more efficiently in O(n) time.
