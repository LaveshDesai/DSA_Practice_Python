# LeetCode 189: Rotate Array

## Approach 1: Using Extra Space (Brute Force)

In this approach, I store the last `k` elements in a temporary array. Then, I shift the remaining elements to the right by `k` positions and place the stored elements at the beginning of the array.

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)

        def rotatebyK(nums, n, k):

            k = k % n

            # Store last k elements
            temp = []

            for i in range(n - k, n):
                temp.append(nums[i])

            # Shift remaining elements to the right
            for i in range(n - k - 1, -1, -1):
                nums[i + k] = nums[i]

            # Place stored elements at the beginning
            j = 0

            for i in range(k):
                nums[i] = temp[j]
                j += 1

            return nums

        rotatebyK(nums, n, k)
```

### Example

Input:

```python
nums = [1,2,3,4,5,6,7]
k = 3
```

Output:

```python
[5,6,7,1,2,3,4]
```

### Dry Run

Original Array:

```text
[1,2,3,4,5,6,7]
```

Store last `k` elements:

```text
temp = [5,6,7]
```

Shift remaining elements:

```text
[1,2,3,4,1,2,3]
```

Place stored elements at the beginning:

```text
[5,6,7,1,2,3,4]
```

### Logic

- First, store the last `k` elements in a temporary array.
- Shift the first `n-k` elements to the right by `k` positions.
- Copy the stored elements back into the first `k` positions.
- This produces the required rotated array.

### Why Do We Use `k = k % n`?

If `k` is greater than the size of the array, rotating `k` times would perform unnecessary rotations.

For example:

```text
n = 7
k = 10
```

```text
10 % 7 = 3
```

So rotating by `10` positions is the same as rotating by `3` positions.

### Complexity

- **Time Complexity: O(n)** → The array is traversed a constant number of times.
- **Space Complexity: O(k)** → A temporary array is used to store the last `k` elements.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Extra Space (Current) | O(n) | O(k) |
| Reversal Algorithm (Optimal) | O(n) | O(1) |

### Limitation

Although this solution runs in linear time, it uses extra space to store the last `k` elements.

### Interview Follow-up

**Why do we store the last `k` elements first?**

→ These elements would be overwritten during shifting, so they must be saved before modifying the array.

**Why do we shift from right to left?**

→ Shifting from left to right would overwrite values before they are moved.

**Can we solve this without extra space?**

→ Yes. The Reversal Algorithm rotates the array in-place using O(1) extra space.

### Key Learning

Whenever elements are shifted in an array, it is often necessary to temporarily store the elements that would otherwise be overwritten during the operation.
