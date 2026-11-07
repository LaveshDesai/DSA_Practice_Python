# 3Sum - Optimal Approach (Sorting + Two Pointers)

## Problem Statement

Given an integer array `nums`, return all unique triplets:

```python
[nums[i], nums[j], nums[k]]
```

such that:

```python
nums[i] + nums[j] + nums[k] == 0
```

The solution must not contain duplicate triplets.

---

## Intuition

Instead of checking every possible triplet using three nested loops, we can:

1. Sort the array.
2. Fix one element at a time.
3. Use two pointers to find the remaining two elements.

Since the array is sorted:

- If the sum is too small, move the left pointer forward.
- If the sum is too large, move the right pointer backward.
- If the sum is zero, store the triplet and skip duplicates.

This reduces the time complexity from **O(n³)** to **O(n²)**.

---

## Optimal Code

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans
```

---

## Example

### Input

```python
nums = [-1,0,1,2,-1,-4]
```

### After Sorting

```python
[-4,-1,-1,0,1,2]
```

### Output

```python
[[-1,-1,2],[-1,0,1]]
```

---

## How It Works

### Step 1

Sort the array.

```python
[-4,-1,-1,0,1,2]
```

---

### Step 2

Fix one element.

```python
nums[i]
```

For example:

```python
i = 1
nums[i] = -1
```

---

### Step 3

Use two pointers.

```python
left = i + 1
right = n - 1
```

```python
left = 2
right = 5
```

---

### Step 4

Calculate the sum.

```python
nums[i] + nums[left] + nums[right]
```

If:

```python
sum < 0
```

move:

```python
left += 1
```

because a larger value is needed.

If:

```python
sum > 0
```

move:

```python
right -= 1
```

because a smaller value is needed.

If:

```python
sum == 0
```

store the triplet and continue searching.

---

## Why Do We Skip Duplicates?

### For Fixed Element

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

Prevents generating the same triplet multiple times.

---

### For Left Pointer

```python
while left < right and nums[left] == nums[left - 1]:
    left += 1
```

Skips duplicate values.

---

### For Right Pointer

```python
while left < right and nums[right] == nums[right + 1]:
    right -= 1
```

Skips duplicate values.

---

## Time Complexity

### Sorting

```text
O(n log n)
```

### Two Pointer Search

```text
O(n²)
```

### Total

```text
O(n²)
```

The O(n²) part dominates O(n log n).

---

## Space Complexity

```text
O(1)
```

Ignoring the output array.

---

## Comparison with Brute Force

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (3 Loops) | O(n³) | O(1) |
| Optimal (Two Pointers) | O(n²) | O(1) |

---

## Why Is This Better?

For:

```text
n = 3000
```

### Brute Force

```text
3000³
= 27 Billion Operations
```

### Optimal

```text
3000²
= 9 Million Operations
```

The optimal solution performs dramatically fewer operations and easily passes the constraints.

---

## Interview Answer

The optimal solution first sorts the array and then fixes one element at a time. For the remaining part of the array, it uses the Two Pointer technique to find pairs whose sum equals the negative of the fixed element. Since each element is processed once with two pointers, the overall time complexity becomes **O(n²)** instead of **O(n³)**. Duplicate values are skipped to ensure that only unique triplets are returned.
