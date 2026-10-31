class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1
            while j < (len(nums)):
                if (nums[i] + nums[j]) == target:
                    arr = []
                    arr.append(i), arr.append(j)
                    return arr
                j += 1
