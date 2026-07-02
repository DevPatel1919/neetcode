class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 4, 6]
        #pref = [1, 1, 2, 8]
        #suff = [48, 24, 6, 1]

        prod = len(nums)
        res = [0] * prod
        suffix = [0] * prod
        prefix = [0] * prod

        prefix[0] = suffix[prod - 1] = 1
        
        for i in range(1, prod):
            prefix[i] = nums[i - 1] * prefix[i-1]
        for i in range(prod-2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(prod):
            res[i] = prefix[i] * suffix[i]

        return res