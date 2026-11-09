# Sort Colors - Brute Force Approach

## Problem Statement

Given an array `nums` containing only:

```text
0 → Red
1 → White
2 → Blue
```

Sort the array in-place so that objects of the same color are adjacent and arranged in the order:

```text
0 → 1 → 2
```

You must modify the input array directly.

---

## Brute Force Idea

Since the array contains only three distinct values (`0`, `1`, and `2`), we can:

1. Count the number of `0`s, `1`s, and `2`s.
2. Overwrite the array with the counted numbers in sorted order.

---

## Algorithm

### Step 1

Count the frequency of:

```python
0
1
2
```

using three counters.

### Step 2

Fill the array with:

```python
countZero times -> 0
countOne times -> 1
countTwo times -> 2
```

---

## Code

```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:

        n = len(nums)

        countZero = 0
        countOne = 0
        countTwo = 0

        for i in range(n):
            if nums[i] == 0:
                countZero += 1
            elif nums[i] == 1:
                countOne += 1
            else:
                countTwo += 1

        i = 0

        while countZero > 0:
            nums[i] = 0
            i += 1
            countZero -= 1

        while countOne > 0:
            nums[i] = 1
            i += 1
            countOne -= 1

        while countTwo > 0:
            nums[i] = 2
            i += 1
            countTwo -= 1
```

---

## Example

### Input

```python
nums = [2,0,2,1,1,0]
```

### Counting Phase

```text
0 → 2 times
1 → 2 times
2 → 2 times
```

### After Overwriting

```python
[0,0,1,1,2,2]
```

### Output

```python
[0,0,1,1,2,2]
```

---

## Time Complexity

### Counting Elements

```text
O(n)
```

### Rewriting Array

```text
O(n)
```

### Overall

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

### Reason

Only three variables (`countZero`, `countOne`, and `countTwo`) are used to store frequencies. No extra array, HashMap, or additional data structure is required.

---

## Drawback

Although this approach is efficient, it requires two passes over the array:

1. One pass for counting.
2. One pass for rewriting.

The Dutch National Flag Algorithm sorts the array in a single traversal.

---

## Interview Answer

This approach counts the occurrences of `0`, `1`, and `2` and then overwrites the array based on those counts. It runs in **O(n)** time and uses **O(1)** extra space because only three counter variables are maintained throughout the algorithm.
