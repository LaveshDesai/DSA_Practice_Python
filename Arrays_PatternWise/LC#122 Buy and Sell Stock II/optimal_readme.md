# LeetCode 122: Best Time to Buy and Sell Stock II

## Optimal Approach: Greedy

In this approach, I take advantage of every profitable price increase.

If today's price is greater than yesterday's price, I add that profit to the answer. Since multiple transactions are allowed, every positive price movement contributes to the maximum profit.

### Code

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maxProfit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                maxProfit += prices[i] - prices[i - 1]

        return maxProfit
```

### Example

Input:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Output:

```python
7
```

Explanation:

```text
Buy at 1, Sell at 5 → Profit = 4
Buy at 3, Sell at 6 → Profit = 3

Total Profit = 7
```

### Logic

- Traverse the array from left to right.
- Compare the current price with the previous price.
- If the current price is greater, add the difference to the profit.
- Ignore decreasing price movements.
- Continue until the end of the array.

### Why It Works

Since multiple transactions are allowed, every increasing price movement can be considered a profit.

For example:

```text
1 → 2 → 3 → 4 → 5
```

Profit:

```text
(2 - 1) + (3 - 2) + (4 - 3) + (5 - 4) = 4
```

which is the same as:

```text
5 - 1 = 4
```

Therefore, adding all positive differences gives the maximum possible profit.

### Common Doubt

**Why is the answer 7 and not 8 for `[7,1,5,3,6,4]`?**

Some people think:

```text
Buy at 1, Sell at 5 → Profit = 4
Buy at 5, Sell at 6 → Profit = 1
Buy at 3, Sell at 6 → Profit = 3

Total = 8
```

This is incorrect because the profit from `5 → 6` is already included in the transaction `3 → 6`.

```text
3 → 6 = 3

which is equal to

(5 - 3) + (6 - 5)
= 2 + 1
= 3
```

If we add both `3 → 6` and `5 → 6`, we are counting the same price increase twice.

So the maximum valid profit is:

```text
Buy at 1, Sell at 5 → Profit = 4
Buy at 3, Sell at 6 → Profit = 3

Total Profit = 7
```

### Complexity

- **Time Complexity: O(n)** → The array is traversed only once.
- **Space Complexity: O(1)** → Only a few variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Greedy (Optimal) | O(n) | O(1) |

### Improvement Over Brute Force

- No nested loops are required.
- Every element is visited only once.
- Makes use of the fact that multiple transactions are allowed.
- Reduces the time complexity from **O(n²)** to **O(n)**.

### Interview Follow-up

**Why do we add only positive differences?**

→ Negative differences would reduce the profit, so they are ignored.

**Why does the greedy approach work?**

→ Every profitable price increase contributes to the final answer, and adding all such increases gives the maximum profit.

**How is this different from LeetCode 121?**

→ LeetCode 121 allows only one transaction, while LeetCode 122sactions.

### Key Learning

When multiple transactions are allowed, every positive price increase can be added to the profit. This observation leads to a simple greedy solution that runs in O(n) time and O(1) space.
