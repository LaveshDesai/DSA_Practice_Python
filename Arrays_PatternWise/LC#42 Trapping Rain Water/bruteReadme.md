
# LC 42 - Trapping Rain Water - Brute Force Approach

## Problem Statement

Given an integer array `height` representing an elevation map where the width of each bar is `1`, calculate how much rainwater can be trapped between the bars.

Return the total amount of trapped rainwater.

---

## Brute Force Idea

The simplest approach is to calculate how much water can be trapped at every index individually.

For each index `i`, we find:

- `leftMax` = Maximum height from index `0` to `i`.
- `rightMax` = Maximum height from index `i` to `n-1`.
- The minimum of `leftMax` and `rightMax` determines the water level.
- Subtract the current bar height to calculate trapped water.
- Add the trapped water to `totalWater`.

### Water Formula

```python
water = min(leftMax, rightMax) - height[i]
```

Where:

- `leftMax` = Maximum height on the left side, including current index.
- `rightMax` = Maximum height on the right side, including current index.
- `height[i]` = Current bar height.

---

## Brute Force Code

```python
class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        totalWater = 0

        for i in range(n):
            leftMax = 0
            rightMax = 0

            for j in range(i, n):
                rightMax = max(rightMax, height[j])

            for j in range(0, i + 1):
                leftMax = max(leftMax, height[j])

            totalWater += min(leftMax, rightMax) - height[i]

        return totalWater
```

---

## Why Do We Use `range(n)`?

```python
for i in range(n):
```

- Iterates through every index of the elevation map.
- Each index represents a position where water might be trapped.
- We calculate the trapped water independently for every index.

---

## Why Do We Use `range(i, n)`?

```python
for j in range(i, n):
    rightMax = max(rightMax, height[j])
```

- Starts from the current index `i`.
- Checks all the bars towards the right side.
- Finds the maximum height on the right, including the current bar.

---

## Why Do We Use `range(0, i + 1)`?

```python
for j in range(0, i + 1):
    leftMax = max(leftMax, height[j])
```

- Starts from index `0`.
- Checks all the bars up to the current index `i`.
- Finds the maximum height on the left, including the current bar.
- `i + 1` is used because the ending index in Python's `range()` is exclusive.

---

## Example

### Input

```python
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

### Output

```python
6
```

### Explanation

The total trapped water is calculated at every index.

For example, consider index `5`:

```python
height[5] = 0
```

Find the maximum height on the left:

```python
leftMax = max([0, 1, 0, 2, 1, 0]) = 2
```

Find the maximum height on the right:

```python
rightMax = max([0, 1, 3, 2, 1, 2, 1]) = 3
```

Calculate trapped water:

```python
water = min(2, 3) - 0
      = 2
```

Therefore, 2 units of water are trapped at index `5`.

Repeat this calculation for every index and add all the trapped water.

```python
totalWater = 6
```

---

## Time Complexity

### Three Nested Loop Levels (Including Outer Loop)

```text
O(n²)
```

- The outer loop runs `n` times.
- The rightMax loop runs approximately `n` times for each index.
- The leftMax loop also runs approximately `n` times for each index.

Total operations:

```text
n × n + n × n
= 2n²
```

Ignoring constants:

```text
Time Complexity: O(n²)
```

---

## Why Is O(n²) Too Slow?

The constraint is:

```text
1 <= height.length <= 2 * 10⁴
```

For:

```text
n = 20000
```

The approximate number of operations is:

```text
20000 × 20000
= 400,000,000

= 400 Million
```

More precisely, the total number of height comparisons is approximately:

```text
n(n+1)
= 20000 × 20001
= 400,020,000
```

Checking approximately 400 million elements is expensive and may result in a **Time Limit Exceeded (TLE)** error.

---

## Space Complexity

```text
O(1)
```

- Only a few variables are used (`n`, `totalWater`, `leftMax`, `rightMax`, `i`, `j`).
- No additional arrays, lists, or sets are created.
- Therefore, auxiliary space complexity is O(1).

---

## Drawbacks of the Brute Force Approach

- Uses nested loops to find leftMax and rightMax.
- Recalculates maximum heights repeatedly.
- Performs unnecessary comparisons.
- Does not scale efficiently for large input sizes.
- May cause Time Limit Exceeded (TLE).

---

## Better Approach

Use the **Prefix Maximum and Suffix Maximum technique** or the **Two Pointer technique**.

Instead of repeatedly calculating the maximum height on both sides for every index, we can optimize the calculation.

### Complexity

```text
Time Complexity: O(n)
Space Complexity: O(n)  # Prefix and suffix arrays
```


---

## Interview Answer

The brute force approach calculates the maximum height on the left and right sides of every index using two nested loops inside an outer loop. The trapped water at each index is calculated using the formula:

`min(leftMax, rightMax) - height[i]`.

Its time complexity is **O(n²)** because we repeatedly calculate the maximum heights for every index.

For the maximum constraint `n = 20000`, it may require approximately **400 million height comparisons**, which can lead to a Time Limit Exceeded (TLE) error.

Therefore, we can optimize the solution using Prefix/Suffix Maximum arrays or the Two Pointer technique, reducing the time complexity to **O(n)**.
