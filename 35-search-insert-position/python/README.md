# 35 Search Insert Position
Challenge: [Here](https://leetcode.com/problems/search-insert-position/)

Based off of the instructions, I immediately thought of [binary search](https://www.geeksforgeeks.org/binary-search/) using the divide and conquer approach. 

A quick refresher for binary search is as follows, you take a two pointer approach (left and right ends of the array) and the middle index between the two to search. Example:

```js
array = [0, 1, 3, 4, 5, 7, 8, 9, 10] target = 4
// the initial left end is 0
// the initial right end is 10
// mid point is 5 (left - right)//2
```

Since we know our mid point is greater than our target, we can do the following:
- our right pointer takes the value of mid point (5)
- our left pointer remains the same
- our new mid point is now 3

In the next iteration of evaluation, we know that 3 is less than our target, so we'd do the following:
- move our left point to the previous mid point (3)
- our right pointer remains the same
- our mid point now becomes 4, and we've found our target

So this solves half the cases, if the number already exists in the sorted array. If it's not in the array, I'll quickly evaluate to see if it's less than the first item in the array or the last.
Otherwise, during the binary search, before setting new pointers - I will check if the number can slot in before or after mid point.
