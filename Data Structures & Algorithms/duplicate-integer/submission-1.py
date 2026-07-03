class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      my_map = {}

      for elem in nums:
        if elem not in my_map:
            my_map[elem] = 1
        else:
            my_map[elem] += 1
        if my_map[elem] > 1:
            return True
      return False  