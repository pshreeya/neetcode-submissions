class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            #skip non-alphanumeric characters from the left
            while i < j and not s[i].isalnum():
                i += 1
                
            #skip non-alphanumeric characters from the right
            while i < j and not s[j].isalnum():
                j -= 1
                
            #compare the valid characters
            if s[i].lower() != s[j].lower():
                return False
                
            #move both pointers inward for the next comparison
            i += 1
            j -= 1
        return True
                


