class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd1 = []
        odd2 = []
        even1 = []
        even2 = []
        for i in range(len(s1)):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
        
        print(sorted(even1), even2.sort(), odd1.sort(), odd2.sort())
        if sorted(even1) == sorted(even2)and sorted(odd1) == sorted(odd2):
        # if set(even1) == set(even2) and set(odd1) == set(odd2):
            return True
        return False
