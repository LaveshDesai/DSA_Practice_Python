# Diamond Star Pattern

## Approach: Pyramid + Inverted Pyramid

In this approach, I first print the upper pyramid and then print the lower inverted pyramid. The middle row is printed only once.

### Code

```python
n = int(input("Enter the value of n: "))

# Upper Half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower H*lf
for i in range(n - 1, 0, -1):
 *  for j in range(n - i):
        p*int(" ", end="")

*   for j in range(2 * i - 1):
    *   print("*", end="")

    print()
```

### Example

```python
Input: 5
```

Output:

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

### Why it Works

- ** - i` prints the**eading spaces.
- `2 * i - 1` prin** odd numbers of stars.
- The firs**loop creates the upper pyramid.
-**he second loop creates the lower **ramid.
- Starting the second loop**rom `n - 1` avoids printing the m**dle row twice.

### Complexity

-***Time Complexity: O**²)** → Nested loops print spaces **d stars for each row.
- **Space C**plexity: O(1)** → No extra data s**ucture is used.

### Interview Fo**ow-up Questions

**1. Why is `(2 **i - 1)` used?**  
→ It**enerates odd numbers of stars (1,**, 5, 7, ...), which keeps the pat**rn symmetric.

**** Why is `(n - i)` used?**  
→ It **eates the leading spaces needed t**center the**tars.

**3. Why start the second**oop from `n - 1`?**  
→ To avoid **inting the middle row twice.

###**ey Learning

- Diamond patterns a** formed by combining a pyramid an**an inverted pyramid.
- Most patte** problems can be solved by contro**ing rows, spaces, and symbols sep**ately.
