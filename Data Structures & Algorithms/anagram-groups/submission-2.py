class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)
            anag[key].append(word)

        return list(anag.values())
