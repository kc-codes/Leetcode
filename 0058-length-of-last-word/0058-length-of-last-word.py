class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        found = False
        for i in range(len(s)-1, -1, -1):

            if s[i] != " ":
                count += 1
                found = True
            elif found == True:
                break
            
                

        return(count)