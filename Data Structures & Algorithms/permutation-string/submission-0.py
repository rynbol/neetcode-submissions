class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:\
        # if len(s1)>len(s2):
        #     return False

        freq = defaultdict(int)
        for i in s1:
            freq[i]+=1

        for i in range(len(s2)):
            temp = freq.copy()
            j = i

            while j < len(s2) and s2[j] in temp:
                temp[s2[j]] -= 1

                if temp[s2[j]] == 0:
                    del temp[s2[j]]
                elif temp[s2[j]] < 0:
                    break

                j += 1

                if len(temp) == 0:
                    return True

        return False
                
                    