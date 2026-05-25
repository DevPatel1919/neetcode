class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag = {}
        if (len(s) != len(t)): 
            return False
        for letter in s:
            if letter not in anag:
                anag[letter] = 0
            anag[letter] += 1
        for letter in t:
            if letter not in anag:
                return False
            anag[letter] -= 1
        
        for value in anag.values():
            if value != 0:
                return False
        
        return True
            
        