class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        odd1 = {letter: 0 for i, letter in enumerate(s1) if i % 2 == 1}
        odd2 = {letter: 0 for i, letter in enumerate(s2) if i % 2 == 1}
        even1 = {letter: 0 for i, letter in enumerate(s1) if i % 2 == 0}
        even2 = {letter: 0 for i, letter in enumerate(s2) if i % 2 == 0}

        

        for i in range(n):
            if i % 2 == 0:
                even1[s1[i]] += 1
                even2[s2[i]] += 1
            else:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1
        
        return odd1 == odd2 and even1 == even2
                
                
        