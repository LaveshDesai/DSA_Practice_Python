# LeetCode 151: Reverse Words in a String

## Approach 2: Using `strip()`, `split()`, and `join()`

I solved this problem using:

```python
return " ".join(s.strip().split()[::-1])
```

The idea was to remove leading and trailing spaces using `strip()`, split the string into words using `split()`, reverse the words using `[::-1]`, and join them back with a single space.

### Example

```python
Input:    "a good   example"
Output:   "example good a"
Expected: "example good a"
```

### Why it Works

Using `split()` without any argument automatically removes extra spaces between words, so no empty strings are created. The `strip()` is optional here because `split()` already handles leading and trailing spaces.

### Complexity

- **Time Complexity: O(n)** → `strip()`, `split()`, reversing, and `join()` process the string linearly.
- **Space Complexity: O(n)** → Extra space is used for the list of words and the output string.
