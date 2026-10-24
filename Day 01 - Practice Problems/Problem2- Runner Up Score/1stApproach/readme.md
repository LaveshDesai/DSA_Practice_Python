# HackerRank: Runner-Up Score

## Approach 1: Remove Maximum Element Repeatedly

I first solved this problem by finding the maximum element, removing all its occurrences from the list, and then finding the maximum element again.

### Code

```python
arr = list(map(int, input().split()))

mx = max(arr)

while mx in arr:
    arr.remove(mx)

print(max(arr))
```

### Example

```python
Input:    [2, 3, 6, 6, 5]
Output:   5
Expected: 5
```

### Why it Works

First, I find the largest element in the list. Then I remove all occurrences of that element. Once all maximum values are removed, the new maximum becomes the runner-up (second largest distinct element).

### Complexity

- **Time Complexity: O(n²)** → `in` and `remove()` both take O(n) time and may run multiple times for duplicate maximum values.
- **Space Complexity: O(1)** → No extra data structure is used; modifications are done on the same list.

### Limitation

This approach works correctly but is not optimal because repeatedly removing elements from a list is expensive for large inputs.
