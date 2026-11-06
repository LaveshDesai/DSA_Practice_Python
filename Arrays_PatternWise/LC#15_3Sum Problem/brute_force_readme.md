# 3Sum Problem - Brute Force Approach

## Problem Statement

Given an integer array `nums`, find all unique triplets:

```python
[nums[i], nums[j], nums[k]]
```

such that:

```python
i != j
i != k
j != k
```

and

```python
nums[i] + nums[j] + nums[k] == 0
```

The result should not contain duplicate triplets.

---

## Brute Force Idea

The simplest way is to check every possible triplet in the array.

Use:

- First loop for the first element.
- Second loop for the second element.
- Third loop for the third element.

For every triplet, check whether the sum is equal to `0`.

If the sum is `0`, store the triplet while avoiding duplicates.

---

## Brute Force Code

```python
ans = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = sorted([nums[i], nums[j], nums[k]])
                ans.add(tuple(temp))

print(list(ans))
```

---

## Example

### Input

```python
nums = [-1, 0, 1, 2, -1, -4]
```

### Output

```python
[[-1, -1, 2], [-1, 0, 1]]
```

### Explanation

Valid triplets are:

```python
(-1) + (-1) + 2 = 0
(-1) + 0 + 1 = 0
```

---

## Time Complexity

### Three Nested Loops

```text
O(n³)
```

Each loop runs approximately `n` times:

```text
n × n × n = n³
```

---

## Why Is O(n³) Too Slow?

According to the constraints:

```text
n <= 3000
```

For:

```text
n = 3000
```

Number of operations:

```text
3000 × 3000 × 3000
= 27,000,000,000
= 27 Billion
```

Checking 27 billion combinations takes too much time and will usually cause a **Time Limit Exceeded (TLE)** error.

---

## Space Complexity

```text
O(1)
```

Ignoring the output storage.

If duplicate handling uses a set:

```text
O(k)
```

where `k` is the number of unique triplets stored.

---

## Drawback of Brute Force

- Uses three nested loops.
- Checks many unnecessary combinations.
- Very slow for large inputs.
- Fails for the maximum constraint due to `O(n³)` complexity.

---

## Better Approach

Sort the array and use the Two Pointer technique.

### Complexity

```text
Time Complexity: O(n²)
Space Complexity: O(1)
```

---

## Interview Answer

The brute force solution uses three nested loops to check every possible triplet, resulting in a time complexity of **O(n³)**. For the maximum constraint `n = 3000`, it may perform up to **27 billion operations**, which is too slow and can lead to a **Time Limit Exceeded (TLE)** error. Therefore, an optimized **O(n²)** solution using sorting and the Two Pointer technique is preferred.
