class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create sets for both s and t and compare them 
        # If they have the same values it returns true otherwise false
        return sorted(s) == sorted(t)
