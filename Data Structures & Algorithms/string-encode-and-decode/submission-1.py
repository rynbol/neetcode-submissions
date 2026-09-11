class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            n = len(i)
            res += str(n) 
            res += "#"
            res += i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        n = len(s)
        curr = ""
        while i < n:
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + length + 1
            j = i
        return res
