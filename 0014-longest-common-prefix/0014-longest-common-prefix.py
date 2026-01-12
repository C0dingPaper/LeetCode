class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 1) Isolate the first word
        first = strs[0]
        # 2) Start looping the first word in (index,value) pairs
        for index, character in enumerate(first):
        # 3) Now start looping the other words
            for s in strs[1:]:
        # 4*) Error checking 
                if index == len(s) or s[index] != character:
                    return first[:index]
        return first 
