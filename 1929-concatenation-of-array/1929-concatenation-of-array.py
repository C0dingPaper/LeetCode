class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Create an array of fixed number of elements
        shift = len(nums)
        length = len(nums)*2
        ans = [None]*length
        # Loop through the first array 
        # For each number 1) insert it in the same pos found in nums
        # Than insert it in the position nums + n
        # Return the full array (which idk how to do with return)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+shift] = nums[i]
        return ans