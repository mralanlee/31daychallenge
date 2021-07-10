# 20 Valid Parentheses
Challenge: [Here](https://leetcode.com/problems/valid-parentheses/)

## Approach
I believe this has to be pretty much a linear scan until a discrepency is found. The good news we have a small finite amount of variables we will face, thus we will create a dictionary.
```python
        bracket_dict = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

```

As we're iterating through, we can put each character up for evaluation into a [stack](https://www.geeksforgeeks.org/stack-data-structure/) and pop each one for evaluation to see if a match pops up.

