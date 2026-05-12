class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # [[1,3],[2,4],[10,11],[10,12],[8,9]]
        #  2      2     1       2       1
        # 1 + 2 + 10 + 10 + 8 = 31
        # 3 + 4 + 11 + 12 + 9 = 39

        # 10 (12) + 10 (11) + 8 (9) + 2 (4) + 1 (3) 
        # 
        tasks.sort(key=lambda x: (-(x[1] - x[0])))
        curr = 0
        res = 0
        for actual, minimum in tasks:
            if curr < minimum:
                res += (minimum - curr)
                curr = minimum
            curr -= actual
        return res
        