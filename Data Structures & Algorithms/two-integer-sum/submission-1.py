class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # num : index

        for i, num in enumerate(nums):
            remaining_val = target - num
            if remaining_val in prevMap:
                return [prevMap[remaining_val], i]
            else:
                prevMap[num] = i