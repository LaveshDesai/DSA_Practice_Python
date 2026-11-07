# 3Sum - Better Approach (HashMap / Hash Set)

## Intuition

Instead of using three nested loops, we can use:

- One loop to fix the first element.
- One loop to find the second element.
- A HashSet to quickly check whether the third element already exists.

The idea is based on:

```text
a + b + c = 0
```

If:

```text
a = nums[i]
b = nums[j]
```

then:

```text
c = -(a + b)
```

We calculate the required third element and check whether it has already been seen using a HashSet.

This reduces the complexity from **O(n³)** to **O(n²)**.

---

## Code

```python
class Solution:
    def threeSum(self, nums):
        ans = set()
        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i + 1, n):

                third = -(nums[i] + nums[j])

                if third in seen:
                    temp = sorted([nums[i], nums[j], third])
                    ans.add(tuple(temp))

                seen.add(nums[j])

        return [list(triplet) for triplet in ans]
```

---

## How It Works

### Input

```python
nums = [-1,0,1,2,-1,-4]
```

---

### Fix First Element

```python
nums[i] = -1
```

---

### Select Second Element

```python
nums[j] = 0
```

---

### Calculate Required Third Element

```python
third = -(-1 + 0)

third = 1
```

Now we check:

```python
if 1 in seen
```

If yes, we found a valid triplet:

```python
[-1, 0, 1]
```

---

## Example Walkthrough

```python
nums = [-1,0,1]
```

### Step 1

```python
i = 0
nums[i] = -1
```

Initialize:

```python
seen = {}
```

---

### Step 2

```python
j = 1
nums[j] = 0
```

Required value:

```python
third = 1
```

Not present in seen.

Add:

```python
seen = {0}
```

---

### Step 3

```python
j = 2
nums[j] = 1
```

Required value:

```python
third = 0
```

```python
0 in seen
```

True.

Triplet found:

```python
[-1,0,1]
```

---

## Why Do We Sort Before Storing?

Consider:

```python
[-1,0,1]
```

and

```python
[0,-1,1]
```

Both represent the same triplet.

To avoid duplicates:

```python
temp = sorted([nums[i], nums[j], third])
```

Then store:

```python
ans.add(tuple(temp))
```

A set automatically removes duplicates.

---

## Time Complexity

### Outer Loop

```text
O(n)
```

### Inner Loop

```text
O(n)
```

### HashSet Lookup

```text
O(1)
```

Average case.

### Total

```text
O(n²)
```

---

## Space Complexity

```text
O(n)
```

For the HashSet.

---

## Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (3 Loops) | O(n³) | O(1) |
| HashMap / HashSet | O(n²) | O(n) |
| Sorting + Two Pointers | O(n²) | O(1) |

---

## Which Solution Is Better?

### HashSet Approach

✅ Easy to understand

✅ Better than brute force

✅ O(n²) time complexity

❌ Uses extra space O(n)

---

### Two Pointer Approach

✅ O(n²) time complexity

✅ O(1) extra space

✅ Most commonly accepted optimal solution in interviews

❌ Requires sorting

---

## Interview Answer

The HashSet approach fixes one element and uses a second loop to select another element. The required third element is calculated using:

```text
third = -(nums[i] + nums[j])
```

A HashSet is used to check in O(1) time whether the third element has already been seen. This reduces the time complexity from **O(n³)** to **O(n²)** at the cost of **O(n)** extra space. Although efficient, the Two Pointer approach is generally considered more optimal because it achieves the same O(n²) time complexity with O(1) extra space.
