# Move Zeroes - Optimal Approach (Two Pointers)

## Problem Statement

Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements.

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

Maintain a pointer called `start`.

```python
start = 0
```

This pointer represents the position where the next non-zero element should be placed.

---

### Step 2

Traverse the array from left to right.

```python
for i in range(n):
```

---

### Step 3

Whenever a non-zero element is found:

```python
if a[i] != 0:
```

swap it with the element at index `start`.

```python
a[i], a[start] = a[start], a[i]
```

This places the non-zero element in its correct position.

---

### Step 4

Move the `start` pointer forward.

```python
start += 1
```

This ensures that the next non-zero element is placed immediately after the previous one.

---

### Step 5

Continue until the entire array has been traversed.

By the end:

- All non-zero elements are shifted to the left.
- All zeroes automatically move to the right.
- The relative order of non-zero elements remains unchanged.

---

## Code

```python
def moveZeros(n: int, a: [int]) -> [int]:

    start = 0

    for i in range(n):

        if a[i] != 0:

            a[i], a[start] = a[start], a[i]
            start += 1

    return a
```

---

## Dry Run

### Input

```python
a = [0,1,0,3,12]
```

### Initial State

```python
start = 0
```

---

### i = 0

```python
a[0] = 0
```

Do nothing.

---

### i = 1

```python
a[1] = 1
```

Swap:

```python
a[1], a[0] = a[0], a[1]
```

Array:

```python
[1,0,0,3,12]
```

```python
start = 1
```

---

### i = 3

```python
a[3] = 3
```

Swap:

```python
a[3], a[1] = a[1], a[3]
```

Array:

```python
[1,3,0,0,12]
```

```python
start = 2
```

---

### i = 4

```python
a[4] = 12
```

Swap:

```python
a[4], a[2] = a[2], a[4]
```

Array:

```python
[1,3,12,0,0]
```

```python
start = 3
```

---

### Output

```python
[1,3,12,0,0]
```

---

## Time Complexity

```text
O(n)
```

### Reason

The array is traversed only once.

```python
for i in range(n):
```

Each element is processed exactly one time.

---

## Space Complexity

```text
O(1)
```

### Reason

Only one extra variable is used:

```python
start
```

No extra array, HashMap, or additional data structure is required.

---

## Comparison with Brute Force Approach

### Brute Force Approach

1. Create a separate array.
2. Store all non-zero elements.
3. Count the number of zeroes.
4. Append zeroes at the end.

#### Complexity

```text
Time Complexity  : O(2n) ≈ O(n)
Space Complexity : O(n)
```

Reason:

- One traversal to collect non-zero elements.
- Another traversal to append zeroes.
- Uses an extra array.

---

### Optimal Two-Pointer Approach

1. Use a pointer `start`.
2. Traverse the array once.
3. Place non-zero elements at their correct positions using swapping.

#### Complexity

```text
Time Complexity  : O(n)
Space Complexity : O(1)
```

Reason:

- Only one traversal is required.
- No extra array is used.
- Sorting is done in-place.

---

## Comparison Table

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (Extra Array) | O(2n) ≈ O(n) | O(n) |
| Optimal (Two Pointers) | O(n) | O(1) |

---

## Why Is This Approach Better?

Although both approaches have an overall time complexity of O(n), the brute force solution requires extra memory to store non-zero elements. The two-pointer approach modifies the original array directly and uses only constant extra space, making it more efficient and optimal.

---

## Interview Answer

The optimal solution uses a pointer `start` to track the position where the next non-zero element should be placed. While traversing the array, every non-zero element is swapped with the element at `start`, and `start` is advanced. This shifts all non-zero elements to the left while pushing zeroes to the right. The algorithm requires only one traversal, resulting in **O(n)** time complexity and **O(1)** extra space complexity.
