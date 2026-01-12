class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and target == nums[i] + nums[j]:
                    if i < j:
                        arr.append(i)
                        arr.append(j)
                        return arr
                    else:
                        arr.append(j)
                        arr.append(i)
                        return arr


        