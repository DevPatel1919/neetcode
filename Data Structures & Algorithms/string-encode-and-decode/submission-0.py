class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        # strs = ["Wow", "Amazing", "Great"]
        # encoded = "3#wow7#amazing5#great"

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            wordlen = int(s[i:j])
            wordstart = j + 1
            wordend = wordstart + wordlen

            decoded.append(s[wordstart:wordend])

            i = wordend

        return decoded

                

