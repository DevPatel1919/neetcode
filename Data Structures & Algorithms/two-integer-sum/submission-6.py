class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in summ:
                return [summ[complement], i]
            
            summ[nums[i]] = i
            
            
        
        