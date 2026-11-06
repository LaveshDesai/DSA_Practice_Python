# LeetCode 167: Two Sum II - Input Array Is Sorted

## Approach 1: Brute Force

My initial approach was to check every possible pair of elements in the array and see if their sum is equal to the target.

I used two nested loops:

- The first loop selects the first number.
- The second loop selects the second number after the first.
- For every pair, I calculate the sum and compare it with the target.
- If the sum matches the target, I return the 1-based indices.

### Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n - 1):
            for j in range(i + 1, n):

                total = numbers[i] + numbers[j]

                if total == target:
                    return [i + 1, j + 1]
```

### Example

Input:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Output:

```python
[1, 2]
```

### Logic

- Start with the first element.
- Pair it with every element after it.
- Calculate the sum of the pair.
- If the sum equals the target, return the indices.
- Since the problem requires 1-based indexing, return `i + 1` and `j + 1`.

### Complexity

- **Time Complexity: O(n²)** → Every pair of elements is checked using two nested loops.
- **Space Complexity: O(1)** → No extra data structure is used.

### Limitation

Although the array is sorted, this approach does not take advantage of that fact. It still checks every possible pair, which makes it inefficient for large inputs.

### Interview Follow-up

**Why does the second loop start from `i + 1`?**

→ To avoid checking the same element twice and to avoid repeating pairs that have already been checked.

**Why do we return `i + 1` and `j + 1`?**

→ The problem requires 1-based indexing instead of 0-based indexing.

**Can we do better because the array is already sorted?**

→ Yes. Since the array is sorted, we can use the Two Pointers approach and solve it in O(n) time.
 
