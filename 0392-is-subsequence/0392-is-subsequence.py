class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for ch in t:
            if index < len(s) and ch == s[index]:
                index+=1
        return index == len(s)
        
        
        # # You advnace the index in s ONLY IF i see the same char in s also in t 
        # # Return the statement if index matches len s that means that it outputs true otherwise false
        # index = 0
        # for ch in t:
        #     if index < len(s) and s[i] == ch:
        #         i+=1
        # return index == len(s)

