# LeetCode 26: Remove Duplicates from Sorted Array

## Optimal Approach: Two Pointers

Since the array is already sorted, duplicate elements always appear next to each other.

I use two pointers:

- `i` traverses the array and checks every element.
- `k` keeps track of the position where the next unique element should be placed.

Whenever a new unique element is found, it is copied to index `k`, and then `k` is incremented.

### Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
```

### Example

Input:

```python
nums = [1, 1, 2]
```

Modified Array:

```python
[1, 2, _]
```

Output:

```python
2
```

### Logic

- Start with `k = 1` because the first element is always unique.
- Traverse the array from index `1`.
- If the current element is different from the previous element, it is a unique element.
- Store that unique element at index `k`.
- Increment `k` to point to the next available position.
- At the end, the first `k` positions contain all unique elements.

### Why Do We Write `nums[k] = nums[i]`?

The problem requires modifying the array in-place.

If we only increased `k`:

```python
k += 1
```

the count would be correct, but the array would still contain duplicates.

By doing:

```python
nums[k] = nums[i]
```

we move each unique element to the correct position in the front part of the array.

### Complexity

- **Time Complexity: O(n)** → The array is traversed only once.
- **Space Complexity: O(1)** → No extra data structure is used.

### Interview Follow-up

**Why does this approach work only because the array is sorted?**

→ Duplicate values are adjacent in a sorted array, making them easy to identify by comparing with the previous element.

**What does `k` represent?**

→ `k` represents both the count of unique elements and the next position where a unique element should be stored.

**Why don't we just increase `k` when we find a unique element?**

→ The problem requires the array to be modified in-place, so unique elements must be moved to the front of the array.

### Key Learning

When a problem asks to modify a sorted array in-place, the Two Pointers technique is often the most efficient solution because it achieves **O(n)** time and **O(1)** space.
