class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        gram = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in gram:
                gram[i] = 0
            gram[i] += 1
        for i in t:
            if i not in gram:
                return False
            else:
                gram[i] -= 1
        
        for value in gram.values():
            if value != 0:
                return False

        return True