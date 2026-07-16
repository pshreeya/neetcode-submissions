class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_set = set() #.add() #.remove()
        left = 0
        max_len = 0

    
        for right in range(len(s)):
            #if we see a duplicate, shrink the window from the left
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            
            #add the new character to the window
            hash_set.add(s[right])
            
            #update max_len if the current window is larger
            max_len = max(max_len, right - left + 1)

        return max_len

                


