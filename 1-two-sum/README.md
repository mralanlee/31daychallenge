# 1 Two Sum
Challenge: [Here](https://leetcode.com/problems/two-sum/)

## Approach
This is a linear scan (left to right), and I use a hashmap to keep a history on the difference between the target and the current number.

For the way, I use `history` - I use as the number you're looking for. In example `nums = [1,3,5,8] and target=4`. Here are the iterations:

```python
history = {}
if 1 in history: ''' false '''
  ''' nothing happens here '''
else:
  history[4 - 1] = i 
  ''' 
    history[3] = 0. 
    So if the next iteration(s) is a 3, then it will tell me that the 1 (to make the sum of the target) is at index 0.
    Now I need to increment i which is the tracker for my index
  '''
```
