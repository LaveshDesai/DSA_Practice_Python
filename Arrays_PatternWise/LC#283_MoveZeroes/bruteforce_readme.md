# Move Zeroes - Brute Force Approach

## Problem Statement

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

### Example

#### Input

```python
nums = [0,1,0,3,12]
```

#### Output

```python
[1,3,12,0,0]
```

---

## My Thinking Process

### Step 1

Find the length of the original array.

```python
n = len(nums)
```

This helps us determine how many total elements are present.

---

### Step 2

Create an extra array to store all non-zero elements.

```python
nonZero = []
```

Traverse the original array using a loop.

```python
for i in range(n):
```

Whenever a non-zero element is found, store it in the new array.

```python
if nums[i] != 0:
    nonZero.append(nums[i])
```

After this step, the `nonZero` array contains all non-zero elements in their original order.

---

### Step 3

Calculate the number of zero elements.

The number of non-zero elements is:

```python
nZ = len(nonZero)
```

The remaining elements must be zeros.

```python
nO = n - nZ
```

where:

```text
nO = Number of Zeroes
```

---

### Step 4

Append the required number of zeroes to the end of the new array.

```python
while i < nO:
    nonZero.append(0)
    i += 1
```

This ensures that all zeroes are moved to the end.

---

### Step 5

Return the modified array.

```python
return nonZero
```

---

## Code

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> listn = len(nums)
        nonZero = []

        for i in range(n):
            if nums[i] != 0:
                nonZero.append(nums[i])

        nZ = len(nonZero)
        nO = n - nZ

        i = 0

        while i < nO:
            nonZero.append(0)
            i += 1

        return nonZero
```

---

## Dry Run

### Input

```python
nums = [0,1,0,3,12]
```

### After Collecting Non-Zero Elements

```python
nonZero = [1,3,12]
```

### Count Values

```python
n = 5
nZ = 3
nO = 2
```

### Append Zeroes

```python
nonZero = [1,3,12,0,0]
```

### Output

```python
[1,3,12,0,0]
```

---

## Time Complexity

### First Traversal

Collecting non-zero elements:

```python
for i in range(n):
```

Time Complexity:

```text
O(n)
```

---

### Second Traversal

Appending zeroes:

```python
while i < nO:
```

In the worst case:

```python
nums = [0,0,0,0,0]
```

the loop runs `n` times.

Time Complexity:

```text
O(n)
```

---

### Overall Time Complexity

```text
O(n) + O(n)
= O(2n)
```

After removing constants:

```text
O(n)
```

---

## Space Complexity

### Extra Array

```python
nonZero = []
```

In the worst case:

```python
nums = [1,2,3,4,5]
```

the extra array stores all `n` elements.

Therefore:

```text
Space Complexity = O(n)
```

---

## Why Is This Considered a Brute Force Approach?

This solution uses an additional array to store non-zero elements and then appends zeroes separately.

Drawbacks:

- Requires extra space.
- Does not modify the original array in-place.
- Uses an additional data structure.

Because of these reasons, it is not the most optimized solution.

---

## Comparison with the Optimal Approach

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (Extra Array) | O(n) | O(n) |
| Optimal (Two Pointers) | O(n) | O(1) |

### Why Is the Optimal Approach Better?

The optimal solution rearranges elements inside the same array using two pointers.

It:

- Maintains the order of non-zero elements.
- Does not require an extra array.
- Uses only constant extra space.

Therefore, it achieves:

```text
Time Complexity  : O(n)
Space Complexity : O(1)
```

---

## Interview Answer

The idea is to first store all non-zero elements in a separate array while preserving their order. After that, the number of zeroes is calculated and appended to the end of the new array. The solution performs two traversals, resulting in **O(n)** time complexity. However, since an additional array is used to store non-zero elements, the space complexity becomes **O(n)**.
