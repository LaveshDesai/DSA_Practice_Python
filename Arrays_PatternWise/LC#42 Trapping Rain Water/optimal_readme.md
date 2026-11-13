
# LC 42 - Trapping Rain Water - Optimal Approach (Two Pointers)

## Problem Statement

Given an integer array `height` representing an elevation map where the width of each bar is `1`, calculate how much rainwater can be trapped between the bars.

Return the total amount of trapped rainwater.

---

## Optimal Approach - Two Pointer Technique

Instead of calculating the maximum height on the left and right sides for every index using nested loops, we use two pointers to optimize the solution.

We start with two pointers:

- `i` starts from the beginning of the array (`0`).
- `j` starts from the end of the array (`n-1`).
- `leftmax` stores the maximum height encountered from the left side.
- `rightmax` stores the maximum height encountered from the right side.

At every iteration:

- Compare `leftmax` and `rightmax`.
- If `leftmax` is smaller, move the left pointer forward.
- Update `leftmax` with the maximum height encountered.
- Calculate the trapped water at the current index.
- Otherwise, move the right pointer backward.
- Update `rightmax` and calculate the trapped water.
- Add the trapped water to `totalWater`.

Continue until both pointers meet.

---

## Water Formula

```python
water = min(leftmax, rightmax) - height[i]
```

Where:

- `leftmax` = Maximum height encountered from the left.
- `rightmax` = Maximum height encountered from the right.
- `height[i]` = Current bar height.
- The smaller boundary determines the water level.

In the Two Pointer implementation, we process the side with the smaller maximum boundary, so we can directly calculate:

```python
water = leftmax - height[i]
```

or

```python
water = rightmax - height[j]
```

---

## Optimal Code

```python
class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        totalWater = 0

        i, j = 0, n - 1
        leftmax = height[i]
        rightmax = height[j]

        while i < j:

            if leftmax < rightmax:
                i += 1
                leftmax = max(leftmax, height[i])
                totalWater += leftmax - height[i]

            else:
                j -= 1
                rightmax = max(rightmax, height[j])
                totalWater += rightmax - height[j]

        return totalWater
```

---

## Why Do We Use `while i < j`?

```python
while i < j:
```

- `i` represents the left pointer.
- `j` represents the right pointer.
- Both pointers move towards each other.
- We need to process each position only once.
- When both pointers meet, all positions have been processed.

---

## Why Do We Initialize `leftmax` and `rightmax`?

```python
leftmax = height[i]
rightmax = height[j]
```

- `leftmax` stores the maximum height encountered from the left.
- `rightmax` stores the maximum height encountered from the right.
- Initially, both pointers are at the boundaries of the array.
- These variables help us track the maximum boundary heights without repeatedly scanning the array.

---

## Why Do We Compare `leftmax < rightmax`?

```python
if leftmax < rightmax:
```

The smaller maximum boundary determines the amount of water that can be trapped.

### Case 1: Left Maximum Is Smaller

```python
i += 1
leftmax = max(leftmax, height[i])
totalWater += leftmax - height[i]
```

- Move the left pointer forward.
- Update `leftmax` if a taller bar is encountered.
- Calculate the trapped water at the current index.
- Add the water to `totalWater`.

### Case 2: Right Maximum Is Smaller or Equal

```python
j -= 1
rightmax = max(rightmax, height[j])
totalWater += rightmax - height[j]
```

- Move the right pointer backward.
- Update `rightmax` if a taller bar is encountered.
- Calculate the trapped water at the current index.
- Add the water to `totalWater`.

---

## Example

### Input

```python
height = [4, 2, 0, 3, 2, 5]
```

### Output

```python
9
```

### Explanation

Initially:

```python
i = 0
j = 5

leftmax = 4
rightmax = 5
```

Since:

```python
leftmax < rightmax
4 < 5
```

We process the left side.

**Step 1:**

```python
i = 1
height[i] = 2

leftmax = max(4, 2) = 4

water = 4 - 2 = 2
totalWater = 2
```

**Step 2:**

```python
i = 2
height[i] = 0

leftmax = max(4, 0) = 4

water = 4 - 0 = 4
totalWater = 6
```

**Step 3:**

```python
i = 3
height[i] = 3

leftmax = max(4, 3) = 4

water = 4 - 3 = 1
totalWater = 7
```

**Step 4:**

```python
i = 4
height[i] = 2

leftmax = max(4, 2) = 4

water = 4 - 2 = 2
totalWater = 9
```

Therefore:

```python
Maximum Trapped Water = 9
```

---

## Time Complexity

### While Loop

```text
O(n)
```

- Both pointers start at opposite ends.
- In every iteration, either the left or right pointer moves.
- Each index is processed at most once.
- Therefore, the loop runs at most O(n) times.

```text
Time Complexity: O(n)
```

---

## Space Complexity

```text
O(1)
```

- Only a few variables are used (`n`, `totalWater`, `i`, `j`, `leftmax`, `rightmax`).
- No additional arrays, lists, or sets are created.
- Therefore, auxiliary space complexity is O(1).

---

## Why Is O(n) Better Than O(n²)?

The constraint is:

```text
1 <= height.length <= 2 * 10⁴
```

For:

```text
n = 20000
```

### Brute Force

```text
O(n²)

Approximately 400 Million comparisons
```

### Optimal Approach

```text
O(n)

Approximately 20000 iterations
```

The Two Pointer approach avoids repeatedly finding the maximum heights on both sides and processes the array in a single traversal.

---

## Advantages of the Optimal Approach

- Uses the Two Pointer technique.
- Eliminates repeated maximum-height calculations.
- Avoids nested loops.
- Processes each index at most once.
- Efficiently handles large input sizes.
- Reduces time complexity from O(n²) to O(n).
- Uses constant auxiliary space O(1).

---

## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Prefix/Suffix Arrays | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |

---

## Interview Answer

The optimal approach uses the Two Pointer technique. We initialize one pointer at the beginning and another at the end of the array. We also maintain `leftmax` and `rightmax` to track the maximum heights encountered from both sides.

At every iteration, we compare these maximum heights and process the side with the smaller maximum boundary. We update the corresponding maximum height and calculate the trapped water using the difference between the maximum boundary and the current height.

We continue until both pointers meet.

This approach reduces the time complexity from **O(n²) to O(n)** and uses **O(1) auxiliary space**.
