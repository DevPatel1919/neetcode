class Solution:
    def trap(self, height: List[int]) -> int:
        lwall = 0
        rwall = 0
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(n):
            j = -i -1
            maxRight[j] = rwall
            maxLeft[i] = lwall
            lwall = max(lwall, height[i])
            rwall = max(rwall, height[j])

        summ = 0
        for i in range(n):
            pot = min(maxLeft[i], maxRight[i])
            summ += max(0, pot - height[i])
        
        return summ
