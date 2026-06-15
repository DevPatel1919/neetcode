class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag = {}
        if (len(s) != len(t)):
            return False
        
        for i in s:
            if i not in anag:
                anag[i] = 0
            anag[i] += 1
        for j in t:
            if j not in anag:
                return False
            anag[j] -= 1
        
        for value in anag.values():
            if value != 0:
                return False
        return True
            