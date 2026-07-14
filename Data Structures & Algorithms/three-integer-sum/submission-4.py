class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []        
        nums.sort()

        for i in range(len(nums)-2):
            #skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l= i+1
            r= len(nums)-1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r-=1
                
                    #skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    #skip duplicate values for the right pointer
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr_sum < 0:
                    l+=1
                else:
                    r-=1
        return res
            

        
        