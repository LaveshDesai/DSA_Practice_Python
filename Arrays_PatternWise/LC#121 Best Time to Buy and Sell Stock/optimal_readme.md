# LeetCode 121: Best Time to Buy and Sell Stock

## Optimal Approach: Track Minimum Price

In this approach, I keep track of the minimum stock price seen so far and calculate the profit that can be earned if I sell on the current day.

For every price:

- Calculate the profit using the current minimum price.
- Update the maximum profit if a better profit is found.
- Update the minimum price if a smaller price is found.

### Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        min_price = prices[0]

        for i in range(1, len(prices)):

            curr_profit = prices[i] - min_price

            result = max(curr_profit, result)

            min_price = min(min_price, prices[i])

        return result
```

### Example

Input:

```python
prices = [7,1,5,3,6,4]
```

Output:

```python
5
```

Explanation:

```text
Buy at 1
Sell at 6
Profit = 6 - 1 = 5
```

### Logic

- Start by assuming the first price is the minimum price.
- For each day, calculate the profit if the stock is sold on that day.
- Keep track of the maximum profit found so far.
- Update the minimum price whenever a lower price appears.
- This ensures that buying always happens before selling.

### Why It Works

For every stock price, we already know the lowest price seen before it.

So instead of checking all possible buy-sell combinations, we directly calculate the best profit for the current day using:

```python
current_profit = current_price - minimum_price_so_far
```

This allows us to find the maximum profit in a single traversal.

### Complexity

- **Time Complexity: O(n)** → The array is traversed only once.
- **Space Complexity: O(1)** → Only a few variables are used.

### Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Optimal Solution | O(n) | O(1) |

### Improvement Over Brute Force

- No nested loops are required.
- Every price is visited only once.
- Reduces the time complexity from **O(n²)** to **O(n)**.

### Interview Follow-up

**Why do we initialize `min_price` with `prices[0]`?**

→ The first day is the only price available at the beginning, so it becomes the initial buying price.

**Why do we calculate profit before updating `min_price`?**

→ We want to check the profit using the minimum price seen before the current day.

**What happens if the prices keep decreasing?**

→ No profit can be made, so the answer remains `0`.

### Key Learning

Whenever a problem asks for the maximum profit, minimum loss, or maximum difference between two elements while maintaining order, consider tracking the minimum (or maximum) value seen so far during a single traversal.
