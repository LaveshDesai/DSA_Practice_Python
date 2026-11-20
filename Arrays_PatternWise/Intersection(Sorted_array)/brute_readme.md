# Intersection of Two Sorted Arrays

## Approach 1: Brute Force

In this approach, I compare every element of the first array with the elements of the second array.

I use a visited array (`vis`) to keep track of elements that have already been matched. This prevents the same element from being added multiple times to the intersection result.

### Code

```python
result = []

vis = [0] * m

for i in range(n):

    for j in range(m):

        if arr[i] == brr[j] and vis[j] == 0:

            result.append(arr[i])
            vis[j] = 1
            break

        if arr[i] < brr[j]:
            break

return result
```

### Example

Input:

```python
arr = [1, 2, 2, 3, 4]
brr = [2, 2, 3, 5]
```

Output:

```python
[2, 2, 3]
```

### Logic

- Create a visited array for the second array.
- Traverse each element of the first array.
- Compare it with elements of the second array.
- If a match is found and the element has not been used before:
  - Add it to the result.
  - Mark the element as visited.
- Continue until all possible matches are found.

### Why It Works

The visited array ensures that each element in the second array is used only once.

Example:

```python
arr = [2, 2]
brr = [2]
```

Without the visited array:

```python
[2, 2]
```

would be produced incorrectly.

With the visited array:

```python
[2]
```

is produced correctly.

### Why Do We Use `if arr[i] < brr[j]: break`?

Since both arrays are sorted:

- If `brr[j]` becomes greater than `arr[i]`,
- No future element in `brr` can match `arr[i]`.

Therefore, we can stop searching early and move to the next element.

### Complexity

- **Time Complexity: O(n × m)** → In the worst case, each element of the first array is compared with every element of the second array.
- **Space Complexity: O(m)** → The visited array stores one entry for each element in the second array.

### Limitation

Although the arrays are sorted, this approach does not fully utilize the sorted order and still performs many unnecessary comparisons.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n × m) | O(m) |
| Two Pointers (Optimal) | O(n + m) | O(1) *(excluding output array)* |

### Interview Follow-up

**Why do we need the visited array?**

→ It prevents the same element in the second array from being matched multiple times.

**Why can we break when `arr[i] < brr[j]`?**

→ Because the arrays are sorted, all remaining elements in `brr` will be greater than `arr[i]`.

**Can this problem be solved without a visited array?**

→ Yes. Using the Two Pointers technique, we can find the intersection in O(n + m) time.

### Key Learning

Using a visited array helps avoid duplicate matches, but since the arrays are sorted, the Two Pointers approach is more efficient and is  solution.
