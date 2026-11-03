class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums)+1)]
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for i, c in freq.items():
            count[c].append(i)
        
        result = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result