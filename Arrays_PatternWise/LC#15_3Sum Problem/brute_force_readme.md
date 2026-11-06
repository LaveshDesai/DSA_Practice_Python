# 3Sum - Brute Force Approach

## Problem Statement

Given an integer array `nums`, return all unique triplets:

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

The solution must not contain duplicate triplets.

---

## Brute Force Idea

The simplest approach is to generate all possible triplets and check whether their sum is equal to `0`.

We use three nested loops:

- The first loop selects the first element.
- The second loop selects the second element.
- The third loop selects the third element.
- If the sum of the three elements is `0`, we store the triplet.
- A set can be used to avoid duplicate triplets.

---

## Brute Force Code

```python
ans = set()
n = len(nums)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = sorted([nums[i], nums[j], nums[k]])
                ans.add(tuple(temp))

print(list(ans))
```

---

## Why Do We Use `n-2`, `n-1`, and `n`?

### First Loop

```python
for i in range(n - 2):
```

After selecting `i`, we still need two more elements (`j` and `k`) to form a triplet.

Therefore, `i` must stop at `n-3`.

---

### Second Loop

```python
for j in range(i + 1, n - 1):
```

After selecting `j`, we still need one more element (`k`).

Therefore, `j` must stop at `n-2`.

---

### Third Loop

```python
for k in range(j + 1, n):
```

`k` is the last element of the triplet, so it can go up to the last index (`n-1`).

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

The constraint is:

```text
1 <= nums.length <= 3000
```

For:

```text
n = 3000
```

The number of operations can be approximately:

```text
3000 × 3000 × 3000
= 27,000,000,000
= 27 Billion
```

Checking 27 billion combinations is extremely slow and will usually result in a **Time Limit Exceeded (TLE)** error.

---

## Space Complexity

```text
O(1)
```

Ignoring the output storage.

If a set is used to store unique triplets:

```text
O(k)
```

where `k` is the number of unique triplets.

---

## Drawbacks of the Brute Force Approach

- Uses three nested loops.
- Checks many unnecessary combinations.
- Performs poorly for large inputs.
- Causes Time Limit Exceeded (TLE) for the maximum constraint.

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

The brute force approach uses three nested loops to check every possible triplet. Its time complexity is **O(n³)**. For the maximum constraint `n = 3000`, it may require checking approximately **27 billion combinations**, which is too slow and can lead to a **Time Limit Exceeded (TLE)** error. Therefore, the optimized solution uses sorting and the Two Pointer technique, reducing the complexity to **O(n²)**.
