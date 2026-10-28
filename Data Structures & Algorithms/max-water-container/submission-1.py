class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            most = max(most, area)
            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most

        