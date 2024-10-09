class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Count frequency of items in magazine
        mcount = Counter(magazine)
        print(mcount)

        for i in ransomNote:
            if mcount[i] <= 0:
                return False
            mcount[i] -= 1
        return True
        