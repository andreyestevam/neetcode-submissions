class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        return self.containsDuplicate_h(nums, 0)
    
    def containsDuplicate_h(self, nums: List[int], i):
        # Base case
        if i == len(nums) - 1:
            return False

        # Recursive case
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
        return self.containsDuplicate_h(nums, i+1)