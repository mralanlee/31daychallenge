# 121 Best Time To Buy and Sell Stock
Challenge: [Here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

I do a simple for loop here with a goal of `O(n)`, and it would just go from left to right since this is supposed to be a historical view for the pricing.

The first step was to set a `profit=0` so that it ignores any potential negative cases off of the bat which is why I wouldn't set it to `None` or `null`.
As it scans the array linearly, I am championing two things a new low for the buy price (`minPrice`) and `profit`. `minPrice` is defaulted to the first item in the array and replaced with the lowest item.

Once a difference is found, return the `profit`. 
