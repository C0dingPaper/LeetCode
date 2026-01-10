class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort the strings and if they have different lengths we know its not an anagram
        return sorted(s) == sorted(t)
