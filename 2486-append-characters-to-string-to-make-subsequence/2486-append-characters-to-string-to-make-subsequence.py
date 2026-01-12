class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count: int = 0
        j: int = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j+=1
                count+=1
        return len(t) - count