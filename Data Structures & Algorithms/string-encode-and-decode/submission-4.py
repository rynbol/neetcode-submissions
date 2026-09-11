class Solution:

    def encode(self, strs: List[str]) -> str:
        curr = ""
        for word in strs:
            n = len(word)
            curr += str(n)
            curr += "#"
            curr += word
        return curr
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        curr_word = ""
        length = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            curr_word = s[i:i+length]
            res.append(curr_word)
            i = i+length

        return res    

        # "12", "abc"
        # "2#123#abc         
