class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counting = Counter(nums)
        for vals in counting.values():
            if vals > 1:
                return True

        return False