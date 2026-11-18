# Rotate Array by One Position (Left Rotation)

## Approach

In this approach, I store the first element of the array in a temporary variable. Then, I shift all elements one position to the left. Finally, I place the stored element at the last position.

This effectively rotates the array by one position towards the left.

### Code

```python
def rotateArray(arr: [], n: int) -> []:

    temp = arr[0]

    for i in range(1, n):
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

    arr[n - 1] = temp

    return arr
```

### Example

Input:

```python
arr = [1, 2, 3, 4, 5]
```

Output:

```python
[2, 3, 4, 5, 1]
```

### Logic

- Store the first element in `temp`.
- Shift every element one position to the left.
- Place the stored element at the last index.
- Return the rotated array.

### Dry Run

```text
Array: [1, 2, 3, 4, 5]

temp = 1

After shifting:
[2, 3, 4, 5, 5]

Place temp at the last position:
[2, 3, 4, 5, 1]
```

### Complexity

- **Time Complexity: O(n)** → The array is traversed once to shift the elements.
- **Space Complexity: O(1)** → Only one extra variable (`temp`) is used.

### Interview Follow-up

**Why do we store the first element in a temporary variable?**

→ The first element would be lost during shifting, so it is stored and placed at the end after the shift operation.

**Can this be done without using an extra variable?**

→ Yes, but the solution becomes less readable and more complex. Using one temporary variable is the standard approach.

### Key Learning

Whenever elements need to be shifted in-place, storing the element that would be overwritten is a common technique to avoid losing data.
