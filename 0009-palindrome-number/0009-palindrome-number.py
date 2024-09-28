class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        a = str(x)
        print(type(a))

        if a == a[::-1]:
            return True 
        return False