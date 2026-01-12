class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if i == len(nums)-1:
                    count+=1
                    arr.append(count)
                    return max(arr)
                count += 1
                # flag = True
            if nums[i] != 1:
                # flag = False
                arr.append(count)
                count = 0
        return max(arr)