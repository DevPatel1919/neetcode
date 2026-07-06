class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag = {}

        for i in s:
            if i not in anag:
                anag[i] = 1
            else:
                anag[i] += 1
        
        for j in t:
            if j not in anag:
                return False
            else:
                anag[j] -= 1
        
        for x in anag:
            if anag[x] != 0:
                return False
        return True

        