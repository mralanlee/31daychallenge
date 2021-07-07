class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value : index
        history = {}
        i = 0
        for n in nums:
          if n in history:
            return [history[n], i]
          else:
            history[target - n] = i
            i += 1
