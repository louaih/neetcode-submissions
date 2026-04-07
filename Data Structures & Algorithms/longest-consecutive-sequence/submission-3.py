class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streaks = []
        nums = sorted(set(nums))

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        s = 1
        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] == -1:
                s += 1
                print(s, i)
                if i == len(nums)-2:
                    streaks.append(s)
            else:
                # streak resets
                streaks.append(s)
                s = 1

        return max(streaks)


        