class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            sortedWord = sorted(i)
            sortedString = "".join(sortedWord)
            if sortedString not in anag:
                anag[sortedString] = [i]
            else:
                anag[sortedString].append(i)
        return list(anag.values())
        