# HackerRank: Runner-Up Score

## Optimal Approach: Tracking Largest and Second Largest

In this approach, I maintain two variables, `first` and `second`, to keep track of the largest and second-largest distinct elements while traversing the array only once.

### Code

```python
first = float('-inf')
second = float('-inf')

arr = list(map(int, input().split()))

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second)
```

### Example

```python
Input:    [2, 3, 6, 6, 5]
Output:   5
Expected: 5
```

### Why it Works

Whenever a new maximum element is found, the current maximum is moved to `second`, and the new value becomes `first`. If a number is smaller than `first` but larger than `second`, it becomes the new second-largest element. This ensures duplicates of the maximum value are ignored.

### Improvement from Previous Approaches

- No repeated removals from the list.
- No sorting is required.
- Only a single traversal of the array is needed.
- Uses constant extra space.

### Complexity

- **Time Complexity: O(n)** → The array is traversed exactly once.
- **Space Complexity: O(1)** → Only two variables (`first` and `second`) are used regardless of input size.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Remove Maximum Repeatedly | O(n²) | O(1) |
| Set + Sort | O(n log n) | O(n) |
| Two Variables (Optimal) | O(n) | O(1) |

### Key Learning

- Tracking the largest and second-largest elements during a single pass is the most efficient solution.
- Eliminates the need for sorting or modifying the input array.
- This is the optimal approach for finding the runner-up score or second-largest distinct element.
