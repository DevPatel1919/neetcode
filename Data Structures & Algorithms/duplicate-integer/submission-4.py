class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set(nums)

        if len(nodup) != len(nums):
            return True
        return False
        