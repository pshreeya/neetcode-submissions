class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r]) 

            area = width * height

            #keep track of max area found so far
            max_area = max(max_area, area)
            
            #move the pointer that has the shorter height
            #as the width shrinks, the height needs to increase to yeild larger area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area



        