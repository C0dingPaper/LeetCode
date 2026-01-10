class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #for i in range(len(nums)):
        #    for j in range(1,len(nums)):
        #        if nums[i] == nums[j]:
        #            return True
        #    return False
        return len(nums) != len(set(nums))
        # Since sets contain only single variables if the lengths are different than it     means that there is duplicates