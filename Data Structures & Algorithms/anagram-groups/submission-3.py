class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count) # immutable key to be established in anag defaultdict
            anag[key].append(word)
        
        return list(anag.values())
 