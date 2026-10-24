# LeetCode 125: Valid Palindrome

## Optimal Approach: Two Pointers

I solved this problem by first removing all non-alphanumeric characters and converting the string to lowercase. Then, I used two pointers to compare characters from both ends of the string.

### Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != sreturn False

            i += 1
            j -= 1

        return True
```

### Example

```python
Input:    "A man, a plan, a canal: Panama"
Output:   True
Expected: True
```

### Why it Works

First, I create a new string containing only lowercase alphanumeric characters. Then, using two pointers, I compare the characters from the beginning and the end. If a mismatch is found, the string is not a palindrome. If all characters match, the string is a palindrome.

### Complexity

- **Time Complexity: O(n)** → One pass is used to clean the string and another pass is used for the two-pointer comparison.
- **Space Complexity: O(n)** → Extra space is required to store the cleaned string.

### Key Learning

- `isalnum()` helps remove special characters and spaces.
- `lower()` makes the comparison case-insensitive.
- Two-pointer comparison is the most efficient way to check for a palindrome.
- O(n) time is optimal because every character must be checked at least once.
