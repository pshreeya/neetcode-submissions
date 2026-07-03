class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for letter in s:
            if letter not in s_map:
                s_map[letter] = 1
            else:
                s_map[letter] += 1

        for letter in t:
            if letter not in t_map:
                t_map[letter] = 1
            else:
                t_map[letter] += 1
        
        if s_map == t_map:
            return True
        return False