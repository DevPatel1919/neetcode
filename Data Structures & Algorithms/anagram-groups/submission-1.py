class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            nums = [0] * 26

            for k in s:
                index = ord(k) - ord('a')
                nums[index] += 1
            key = tuple(nums)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)

            anag = list(groups.values())
        return anag


        

