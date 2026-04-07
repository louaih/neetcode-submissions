class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indexes = {}
        # res = []

        # for i in range(len(nums)):
        #     indexes[nums[i]] = indexes.get(nums[i]) + [i] if indexes.get(nums[i],0) else [i]
    
        # for num in indexes.keys():
        #     complement = target - num
        #     if num == complement and len(indexes[num]) < 2:
        #         continue
        #     if indexes.get(complement):
        #         return sorted([indexes[num].pop(), indexes[complement].pop()])

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    return [i, j]