class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)

        while l < r:
            diff = target - numbers[l-1]

            if numbers[r-1] == diff:
                return [l, r]
            elif numbers[r-1] > diff:
                #r is too big, make r pointer smaller
                r -= 1
            else:
                #r is too small, l is too small, make l pointer bigger
                l += 1
        