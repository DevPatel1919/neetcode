class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        for i in t:
            if i not in seen:
                return False
            else:
                seen[i] -= 1
        
        for i in seen:
            if seen[i] != 0:
                return False
        return True
            
            
        