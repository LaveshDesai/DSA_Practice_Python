# LeetCode 26: Remove Duplicates from Sorted Array

## Approach: Using Set

In this approach, I use a set to store only unique elements from the array.

Since a set does not allow duplicate values, all duplicates are automatically removed. After collecting the unique elements, I convert the set back into a list and return it.

### Code

```python
class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        seen = set()

        for i in range(n):
            seen.add(nums[i])

        nums = list(seen)

        return nums


s = Solution()
print(s.removeDuplicates([1,1,2,2,2,3,3]))
```

### Example

Input:

```python
[1,1,2,2,2,3,3]
```

Output:

```python
[1,2,3]
```

### Logic

- Create an empty set.
- Traverse the array and insert every element into the set.
- Duplicate elements are automatically ignored.
- Convert the set back into a list.
- Return the list containing only unique elements.

### Why It Works

A set stores only unique values.

For example:

```python
{1, 1, 2, 2, 3}
```

becomes:

```python
{1, 2, 3}
```

As a result, all duplicate values are removed automatically.

### Complexity

- **Time Complexity: O(nlogn+n)** → Each element is inserted into the set once.
- **Space Complexity: O(n)** → A set is used to store the unique elements.

### Limitation

This approach uses extra space and does not modify the array in-place.

Because of this, it is **not accepted as the optimal solution for LeetCode 26**, where the expected space complexity is **O(1)**.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Set Approach | O(nlogn + n) | O(n) |
| Two Pointers (Optimal) | O(n) | O(1) |

### Interview Follow-up

**Why does a set remove duplicates automatically?**

→ A set stores only unique values, so duplicate insertions are ignored.

**Why is this not the optimal solution for LeetCode 26?**

→ The problem requires the array to be modified in-place using O(1) extra space, while a set uses O(n) extra space.

**Does a set preserve order?**

→ Not necessarily. If maintaining sorted order is important, additional handling may be required.

### Key Learning

Using a set is a simple and efficient way to remove duplicates, but it requires extra memory. For in-place modification problems, the Two Pointers technique is usually preferred.
