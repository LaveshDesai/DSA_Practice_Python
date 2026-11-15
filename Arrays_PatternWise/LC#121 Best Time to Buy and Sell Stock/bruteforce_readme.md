# LeetCode 121: Best Time to Buy and Sell Stock

## Approach 1: Brute Force

My initial approach was to check every possible buy day and sell day.

For each day, I try selling the stock on all future days and calculate the profit. I then keep track of the maximum profit found.

### Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        profit = 0

        for i in range(n):

            for j in range(i + 1, n):

                curr_profit = prices[j] - prices[i]

                profit = max(profit, curr_profit)

        return profit
```

### Example

Input:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Output:

```python
5
```

Explanation:

```text
Buy at 1
Sell at 6
Profit = 5
```

### Logic

- Select every day as a possible buying day.
- Check every future day as a possible selling day.
- Calculate the profit for each pair.
- Store the maximum profit found.

### Complexity

- **Time Complexity: O(n²)** → Every buy day is compared with every possible sell day.
- **Space Complexity: O(1)** → No extra data structure is used.

### Limitation

This approach checks all possible buy-sell pairs, resulting in many unnecessary comparisons for large inputs.

### Interview Follow-up

**Why does the second loop start from `i + 1`?**

→ A stock must be bought before it can be sold.

### Key Learning

Brute force helps us understand the problem by checking all possible combinations before optimizing.
