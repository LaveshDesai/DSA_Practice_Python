
# LC 11 - Container With Most Water - Optimal Approach (Two Pointers)

## Problem Statement

Given an integer array `height` of length `n`, there are `n` vertical lines where the endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

Return the maximum amount of water a container can store.

---

## Optimal Approach - Two Pointer Technique

Instead of checking every possible pair using two nested loops, we use two pointers to reduce the time complexity from O(n²) to O(n).

We start with two pointers:

- `i` starts from the beginning of the array (`0`).
- `j` starts from the end of the array (`n-1`).

At every iteration:

- Calculate the minimum height between the two pointers.
- Calculate the width using the difference between their indices.
- Calculate the area using the formula.
- Update the maximum water if the current area is greater.
- Move the pointer that has the smaller height.

We continue until both pointers meet.

---

## Area Formula

```python
h = min(height[i], height[j])
w = j - i
area = h * w
```

Where:

- `h` = Minimum height of the two lines.
- `w` = Width between the two lines.
- `area` = Amount of water the container can store.

---

## Optimal Code

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        maxWater = 0

        i = 0
        j = n - 1

        while i < j:
            h = min(height[i], height[j])
            w = j - i

            area = h * w

            maxWater = max(area, maxWater)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxWater
```

---

## Why Do We Use `while i < j`?

```python
while i < j:
```

- `i` represents the left pointer.
- `j` represents the right pointer.
- We need two different lines to form a container.
- When both pointers meet, the width becomes `0`.
- Therefore, we stop when `i == j`.

---

## Why Do We Move the Smaller Height Pointer?

```python
if height[i] < height[j]:
    i += 1
else:
    j -= 1
```

The water area depends on two factors:

```python
area = min(height[i], height[j]) * (j - i)
```

The smaller height determines the maximum water level.

### Case 1: Left Height Is Smaller

```python
if height[i] < height[j]:
    i += 1
```

- The left height limits the amount of water.
- Keeping the left pointer fixed and moving the right pointer reduces the width.
- The water height cannot increase beyond the current left height.
- Therefore, we move the left pointer forward to find a potentially taller line.

### Case 2: Right Height Is Smaller or Equal

```python
else:
    j -= 1
```

- The right height limits the amount of water.
- Keeping the right pointer fixed and moving the left pointer reduces the width.
- The water height cannot increase beyond the current right height.
- Therefore, we move the right pointer backward.

**Important:** The array does NOT need to be sorted. We only compare the heights at the current two pointers.

---

## Example

### Input

```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

### Output

```python
49
```

### Explanation

Initially:

```python
i = 0
j = 8

height[i] = 1
height[j] = 7
```

Calculate the area:

```python
h = min(1, 7) = 1
w = 8 - 0 = 8

area = 1 * 8 = 8
```

Since the left height is smaller, move `i` forward.

The algorithm continues calculating areas and moving the smaller-height pointer.

Eventually, the maximum area is found between:

```python
i = 1
j = 8

height[i] = 8
height[j] = 7
```

Calculate:

```python
h = min(8, 7) = 7
w = 8 - 1 = 7

area = 7 * 7 = 49
```

Therefore:

```python
Maximum Water = 49
```

---

## Time Complexity

### While Loop

```text
O(n)
```

- Both pointers start at opposite ends.
- In every iteration, either `i` increases or `j` decreases.
- Each pointer moves towards the other pointer.
- The loop executes at most `n-1` times.

Therefore:

```text
Time Complexity: O(n)
```

---

## Space Complexity

```text
O(1)
```

- Only a few variables are used (`n`, `maxWater`, `i`, `j`, `h`, `w`, `area`).
- No additional data structures are created.
- Therefore, auxiliary space complexity is O(1).

---

## Why Is O(n) Better Than O(n²)?

The constraint is:

```text
2 <= height.length <= 10⁵
```

For:

```text
n = 100000
```

### Brute Force

```text
O(n²)

100000 × 99999 / 2

≈ 5 Billion comparisons
```

### Optimal Approach

```text
O(n)

At most approximately 100000 iterations
```

The Two Pointer approach avoids checking every possible pair and significantly reduces the number of operations.

---

## Advantages of the Optimal Approach

- Uses the Two Pointer technique.
- Eliminates the need for nested loops.
- Does not require a sorted array.
- Checks fewer unnecessary combinations.
- Efficiently handles large input sizes.
- Reduces time complexity from O(n²) to O(n).
- Uses constant auxiliary space O(1).

---

## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |

---

## Interview Answer

The optimal approach uses the Two Pointer technique. We initialize one pointer at the beginning and another at the end of the array. At every iteration, we calculate the area using the minimum height and the width between the two pointers.

We update the maximum water and move the pointer with the smaller height because it limits the water capacity.

This continues until both pointers meet.

The approach reduces the time complexity from **O(n²) to O(n)** and uses **O(1) auxiliary space**.
