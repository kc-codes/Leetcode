class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        x = list(s)
        temp = []
        
        for i in x:
            if i in vowels:
                temp.append(i)
        temp = temp[::-1]

        j = 0
        for i in range(len(x)):
            if x[i] in vowels:
                x[i] = temp[j]
                j +=1
        return "".join(x)
