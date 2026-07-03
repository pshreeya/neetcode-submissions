class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1 
            else:
                dict_s[s[i]] += 1

        for n in range(len(t)):
            if t[n] not in dict_t:
                dict_t[t[n]] = 1 
            else:
                dict_t[t[n]] += 1

        if dict_s == dict_t:
            return True
        else:
            return False
             

