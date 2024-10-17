class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        i = 0
        j = n - 1
        stack = []
        while j > 0:
            if not stack:
                stack.append([j, s[j]])
            elif s[j] > stack[-1][1]:
                stack.append([j, s[j]])
            j -= 1
        while i < n - 1:
            if s[i] < stack[-1][1]:
                break
            if i == stack[-1][0]:
                stack.pop()
            i += 1
        if stack:
            s[i], s[stack[-1][0]] = s[stack[-1][0]], s[i]
        return int("".join(s))