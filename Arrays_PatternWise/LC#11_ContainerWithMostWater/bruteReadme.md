
# LC 11 - Container With Most Water - Brute Force Approach

## Problem Statement

Given an integer array `height` of length `n`, there are `n` vertical lines where the endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

Return the maximum amount of water a container can store.

---

## Brute Force Idea

The simplest approach is to check every possible pair of lines and calculate how much water they can store.

We use two nested loops:

- The first loop selects the first line (`i`).
- The second loop selects the second line (`j`).
- Calculate the width between the two lines.
- Find the minimum height of the two lines.
- Calculate the area using the formula.
- Update the maximum water whenever a larger area is found.

### Area Formula

```python
width = j - i
h = min(height[i], height[j])
area = width * h
```

---

## Brute Force Code

```python
def maxArea(height):
    max_water = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j])

            area = width * h
            max_water = max(max_water, area)

    return max_water
```

---

## Why Do We Use `range(n)` and `range(i + 1, n)`?

### First Loop

```python
for i in range(n):
```

- Selects the first line.
- `i` can start from index `0` and go up to `n-1`.
- We use this line as the starting boundary of the container.

### Second Loop

```python
for j in range(i + 1, n):
```

- Selects the second line.
- `j` starts from `i + 1` to avoid selecting the same line.
- It checks every line after `i`.
- This ensures that every pair is checked only once.

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

The maximum water is formed between:

```python
height[i] = 8
height[j] = 7
```

Their indices are:

```python
i = 1
j = 8
```

Calculate the width:

```python
width = 8 - 1 = 7
```

Calculate the minimum height:

```python
h = min(8, 7) = 7
```

Calculate the area:

```python
area = 7 * 7 = 49
```

Therefore:

```python
Maximum Water = 49
```

---

## Time Complexity

### Two Nested Loops

```text
O(n²)
```

Each loop runs approximately `n` times:

```text
n × n = n²
```

More precisely, the total number of pairs checked is:

```text
n * (n - 1) / 2
```

---

## Why Is O(n²) Too Slow?

The constraint is:

```text
2 <= height.length <= 10⁵
```

For:

```text
n = 100000
```

The number of pairs checked is approximately:

```text
100000 × 99999 / 2
= 4,999,950,000
≈ 5 Billion
```

Checking approximately 5 billion pairs is extremely slow and will usually result in a **Time Limit Exceeded (TLE)** error.

---

## Space Complexity

```text
O(1)
```

- Only a few variables are used (`max_water`, `n`, `i`, `j`, `width`, `h`, `area`).
- No additional array, list, or set is created.
- Therefore, the auxiliary space complexity is O(1).

---

## Drawbacks of the Brute Force Approach

- Uses two nested loops.
- Checks every possible pair of lines.
- Performs many unnecessary comparisons.
- Does not scale well for large input sizes.
- Causes Time Limit Exceeded (TLE) for the maximum constraint.

---


## Interview Answer

The brute force approach uses two nested loops to check every possible pair of lines and calculate the water they can store. Its time complexity is **O(n²)**.

For the maximum constraint `n = 100000`, it may require checking approximately **5 billion pairs**, which is too slow and can lead to a **Time Limit Exceeded (TLE)** error.

Therefore, the optimized solution uses the **Two Pointer technique**, reducing the time complexity from **O(n²) to O(n)** while maintaining O(1) auxiliary space.

