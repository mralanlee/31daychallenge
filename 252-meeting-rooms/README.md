# 252 Meeting Rooms
Challenge: [Here](https://leetcode.com/problems/meeting-rooms/)

## Approach
So this is simplified if you run a `.sort()`, which in Python is a [Timsort](https://leetcode.com/problems/meeting-rooms/) (a variation of quick sort).

After that, it's just a linear scan and you just need to make sure the 1st index of the current iteration does not conflict with the next intervals 0th index.

