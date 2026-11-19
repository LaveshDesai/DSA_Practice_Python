# Union of Two Sorted Arrays

## Approach 1: Using Set (Brute Force)

In this approach, I use a set to store all unique elements from both arrays.

First, I insert all elements from the first array into the set. Then, I insert all elements from the second array. Since a set stores only unique values, duplicate elements are automatically removed.

Finally, I convert the set into a sorted list and return it.

### Code

```python
def sortedArray(a: [int], b: [int]) -> [int]:

    union = []
    set1 = set()

    n1 = len(a)
    n2 = len(b)

    # Insert elements from the first array
    for i in range(n1):
        set1.add(a[i])

    # Insert elements from the second array
    for i in range(n2):
        set1.add(b[i])

    union = sorted(list(set1))

    return union
```

### Example

Input:

```python
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 4, 5, 6]
```

Output:

```python
[1, 2, 3, 4, 5, 6]
```

### Logic

- Create an empty set.
- Insert all elements from the first array.
- Insert all elements from the second array.
- Duplicate values are automatically ignored by the set.
- Convert the set into a sorted list.
- Return the final union array.

### Why It Works

A set stores only unique elements.

For example:

```python
{1, 2, 2, 3, 3, 4}
```

becomes:

```python
{1, 2, 3, 4}
```

After converting the set to a sorted list, we get the required union of the two arrays.

### Complexity

- **Time Complexity: O((n1 + n2) log(n1 + n2))**
  - Inserting elements into the set takes O(n1 + n2).
  - Sorting the unique elements takes O((n1 + n2) log(n1 + n2)).

- **Space Complexity: O(n1 + n2)**
  - In the worst case, all elements are unique and stored in the set.

### Limitation

Although the arrays are already sorted, this approach does not take advantage of the sorted order.

### Interview Follow-up

**Why do we use a set?**

→ A set automatically removes duplicate elements.

**Why do we sort the set before returning?**

→ Sets do not maintain sorted order, but the problem expects the union array to be sorted.

**Can we solve this without using extra space?**

→ We can use the Two Pointers technique because both arrays are already sorted.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Set Approach (Current) | O((n1+n2) log(n1+n2)) | O(n1+n2) |
| Two Pointers (Optimal) | O(n1+n2) | O(n1+n2)* |

\* Space used only for storing the final answer.

### Key Learning

Using a set is a simple way to find the union of two arrays, but when the arrays are already sorted, the Two Pointers approach is more efficient and makes better use of the given information.
