# LeetCode 167: Two Sum II - Input Array Is Sorted

## Optimal Approach: Two Pointers

Since the array is already sorted, I use two pointers:

- One pointer starts from the beginning of the array.
- The other pointer starts from the end of the array.

Based on the current sum:

- If the sum is greater than the target, move the right pointer left.
- If the sum is smaller than the target, move the left pointer right.
- If the sum matches the target, return the indices.

### Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        i, j = 0, n - 1

        while i < j:

            if numbers[i] + numbers[j] > target:
                j -= 1

            elif numbers[i] + numbers[j] < target:
                i += 1

            else:
                return [i + 1, j + 1]
```

### Example

Input:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Output:

```python
[1, 2]
```

### Logic

- Start with two pointers at both ends of the array.
- Calculate the current sum.
- If the sum is too large, decrease it by moving the right pointer.
- If the sum is too small, increase it by moving the left pointer.
- Continue until the target sum is found.

### Why It Works

Because the array is sorted:

- Moving the left pointer increases the sum.
- Moving the right pointer decreases the sum.

This allows us to eliminate unnecessary comparisons and find the answer efficiently.

### Complexity

- **Time Complexity: O(n)** → Each pointer moves at most `n` times.
- **Space Complexity: O(1)** → No extra data structure is used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Two Pointers (Optimal) | O(n) | O(1) |

### Improvement Over Brute Force

- No nested loops are required.
- Takes advantage of the sorted array.
- Reduces the time complexity from **O(n²)** to **O(n)**.

### Interview Follow-up

**Why does the two-pointer approach work only because the array is sorted?**

→ The sorted order allows us to predict how the sum changes when moving either pointer.

**Why do we move the right pointer when the sum is greater than the target?**

→ Moving the right pointer decreases the sum because the array is sorted.

**Why do we move the left pointer when the sum is smaller than the target?**

→ Moving the left pointer increases the sum because the array is sorted.

### Key Learning

Whenever a problem involves a sorted array and finding a pair that satisfies a condition, consider using the Two Pointers technique before thinking about nested loops.
