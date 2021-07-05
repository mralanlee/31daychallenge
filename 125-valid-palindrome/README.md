# 125 Valid Palindrome
Challenge: [Here](https://leetcode.com/problems/valid-palindrome/)

## Approach
The description says to only consider alphanumeric characters and to ignore cases. So my initial approach is to think about doing this as a linear scan. Add a condition to check which characters are alphanumeric (i.e. ignoring `,` or other non-alphanumeric characters).
A cleaner approach would just to split the string, and run a `.filter` method but I was just thinking through the naive approach first.

As I loop through and lowercase all strings (regardless if they are already lower case or not), I concatenate it naively to my `str` variable, and at the end of the loop it will check if the string is equal to it's reverse.

## What I could do differently
The approach above would give me a `O(n)` approach but I do believe I could solve this in `O(log n)` by using a two pointer method, one starting from the left, and another on the right.

It could look something like...
```python

left, right = 0, len(s) - 1
mid = len(s) // 2

while left < right:
  ''' 
  Create two inner loops to scoot the pointers left pointer towards the right if s[left] is not alphanumeric OR
  the right pointer towards the left if s[right] is not alphanumeric

  Once right and left is alphanumeric, we lowercase both s[left] and s[right] at their current positions and see if they're equal, if not return False
  '''
  
  Increment the pointer's both +1 to keep the loop going
```

This should result in a `O(log n)` solution without scanning the entire string in one linear loop.
