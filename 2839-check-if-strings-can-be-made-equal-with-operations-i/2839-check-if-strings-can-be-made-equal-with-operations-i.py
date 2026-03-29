class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        letters = list(s1)
        ex0 = s1
        ex1 = letters[2] + letters[1] + letters[0] + letters[3]
        ex2 = letters[0] + letters[3] + letters[2] + letters[1]
        ex3 = letters[2] + letters[3] + letters[0] + letters[1]
        
        if s2 in (ex0, ex1, ex2, ex3):
            return True
        return False
