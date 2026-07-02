class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        longest = 0

        for con in nums:
            if con - 1  not in consec:
                length = 1
                while (con + length) in consec:
                    length += 1
                    
                longest = max(length, longest)
        
        return longest