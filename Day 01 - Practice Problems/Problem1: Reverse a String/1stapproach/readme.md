# LeetCode 151: Reverse Words in a String

## Approach 1: Using `split()` and `join()`

I first tried solving this problem using:

```python
return " ".join(s.split(" ")[::-1])
```

The idea was to split the string into words, reverse them using `[::-1]`, and join them back with a single space.

### Example

```python
Input:    "a good   example"
Output:   "example   good a"
Expected: "example good a"
```

### Problem

Using `split(" ")` treats every space as a separator, so multiple spaces create empty strings in the list. Because of this, extra spaces appear in the output and the solution fails for such test cases.

### Complexity

- **Time Complexity: O(n)** → `split()`, reversing, and `join()` each process the string once.
- **Space Complexity: O(n)** → Extra space is used for the list of words and the output string.
