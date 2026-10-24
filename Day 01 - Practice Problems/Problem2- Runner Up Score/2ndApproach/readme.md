# HackerRank: Runner-Up Score

## Approach 2: Using `set()` and `sort()`

In this approach, I removed all duplicate values using `set()`, converted the result back to a list, sorted it, and returned the second-last element as the runner-up score.

### Code

```python
arr = list(map(int, input().split()))

arr = list(set(arr))
arr.sort()

print(arr[-2])
```

### Example

```python
Input:    [2, 3, 6, 6, 5]
Output:   5
Expected: 5
```

### Why it Works

`set()` removes duplicate values, ensuring that only distinct elements remain. After sorting the list, the last element is the largest and the second-last element becomes the runner-up score.

### Changes from Approach 1

- Removed duplicates directly using `set()` instead of repeatedly removing the maximum element.
- Used sorting to arrange elements in ascending order.
- Reduced the time complexity from **O(n²)** to **O(n log n)**.

### Complexity

- **Time Complexity: O(n log n)** → Creating the set takes O(n), and sorting the distinct elements takes O(n log n).
- **Space Complexity: O(n)** → Extra space is required to store the set of unique elements.

### Comparison with Approach 1

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Remove Maximum Repeatedly | O(n²) | O(1) |
| Set + Sort | O(n log n) | O(n) |

### Improvement

This approach improves the time complexity significantly by avoiding repeated list traversals and removals. The trade-off is O(n) extra space for storing unique elements.
