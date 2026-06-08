class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                lower.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        return lower + equal + greater 
        