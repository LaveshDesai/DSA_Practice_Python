# Second Largest Element in an Array

## Approach 2: Two Pass Traversal

In this approach, I first find the largest element in the array using a linear traversal. Once the largest element is known, I perform another traversal to find the largest value that is not equal to the largest element.

This avoids sorting the array and improves the time complexity.

### Code

```python
class Solution:
    def secondLargest(self, nums: list[int]) -> int:

        n = len(nums)

        largest = nums[0]

        for i in range(1, n):
            largest = max(largest, nums[i])

        secondLargest = float('-inf')

        for i in range(n):
            if nums[i] != largest:
                secondLargest = max(secondLargest, nums[i])

        return secondLargest
```

### Example

Input:

```python
nums = [1, 3, 4, 2, 8, 8, 6]
```

Output:

```python
6
```

### Logic

#### Pass 1

Find the largest element:

```python
largest = 8
```

#### Pass 2

Find the largest element that is not equal to `largest`.

```python
1, 3, 4, 2, 6
```

The maximum among these values is:

```python
6
```

Therefore:

```python
secondLargest = 6
```

### Why It Works

- The first traversal finds the maximum element in the array.
- The second traversal ignores all occurrences of the largest element.
- Among the remaining elements, the maximum value becomes the second largest element.

### Why Use `float('-inf')`?

```python
secondLargest = float('-inf')
```

This ensures that the algorithm works correctly even when the array contains negative numbers.

Example:

```python
nums = [-5, -2, -8]
```

The second largest element is:

```python
-5
```

Using `0` would produce incorrect results for such cases.

### Complexity

- **Time Complexity: O(n)** → Two separate traversals are performed, each taking O(n). Therefore, O(n + n) = O(n).
- **Space Complexity: O(1)** → Only a few variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Two Pass Traversal | O(n) | O(1) |
| Single Pass Traversal (Optimal) | O(n) | O(1) |

### Improvement Over Sorting

- No sorting is required.
- Avoids unnecessary rearrangement of elements.
- Reduces the time complexity from **O(n log n)** to **O(n)**.

### Interview Follow-up

**Why do we use two traversals?**

→ The first traversal finds the largest element, and the second traversal finds the largest value different from it.

**Why do we check `nums[i] != largest`?**

→ Duplicate occurrences of the largest element should not be considered the second largest element.

**Can we solve this in a single traversal?**

→ Yes. We can maintain both the largest and second largest values simultaneously using two variables.

### Key Learning

When only the largest and second largest elements are required, sorting is unnecessary. A linear traversal can solve the problem more efficiently.
