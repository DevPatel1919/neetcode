class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        maxL = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            maxL = max(maxL, len(seen))
            r += 1
        return maxL
        
        # "xzyzxyz"
          #  l
          #   r


