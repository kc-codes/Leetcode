class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for s in strs:
            k = str(sorted(s))

            if k not in mp:
                mp[k] = []
            mp[k].append(s)
        return(mp.values())
