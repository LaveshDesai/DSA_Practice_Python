# LeetCode 151: Reverse Words in a String

## Optimal Approach: Using `split()` and `join()`

I solved this problem using:

```python
return " ".join(s.split()[::-1])
```

The idea is to split the string into words using `split()`, reverse the list of words using `[::-1]`, and join them back with a single space using `join()`.

### Example

```python
Input:    "a good   example"
Output:   "example good a"
Expected: "example good a"
```

### Why it Works

Using `split()` without any argument automatically removes leading, trailing, and extra spaces between words. After reversing the words, `join()` combines them with exactly one space.

### Complexity

- **Time Complexity: O(n)** → `split()`, reversing, and `join()` each process the string once, so the overall complexity remains linear.
- **Space Complexity: O(n)** → Extra space is used to store the list of words and the final output string.

### Note

This is the optimal solution in Python because every character must be processed at least once, and creating the output string requires O(n) space.
