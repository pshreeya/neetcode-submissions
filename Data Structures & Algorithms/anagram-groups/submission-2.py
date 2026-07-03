class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {}

        for word in strs:
            #if the letters of each word are sorted alphabetically, it's easier to compare
            #anagrams would be the same word
            alphabetical_key = "".join(sorted(word))

            #if key not in map (when you're creating it initially)
            if alphabetical_key not in anagram_map:
                anagram_map[alphabetical_key] = []

            anagram_map[alphabetical_key].append(word)

        #returns all the grouped lists
        return list(anagram_map.values())


                      
                
        

            


        

