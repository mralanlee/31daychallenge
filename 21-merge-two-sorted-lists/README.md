# 21 Merge Two Sorted Lists
Challenge: [Here](https://leetcode.com/problems/merge-two-sorted-lists/)

## Approach
I did the lazy manager approaches where if eventually I hit a point where my inputs `l1` or `l2` were empty, then to just return the current node.

The following logic after the `None` checks are to figure out the placement based on value.

```python
if l1.val < l2.val:
  ''' if it is smaller than set the pointer for the 'next' node to be the next value '''
  l1.next = self.mergeTwoLists(l1.next, l2)
```

