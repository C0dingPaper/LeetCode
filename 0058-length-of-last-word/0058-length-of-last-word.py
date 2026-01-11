class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        s = s.strip()
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                count+=1
            if s[i] == " " and (s[i+1] != " " or s[i+1] == None):
                flag = True
                break
        return count