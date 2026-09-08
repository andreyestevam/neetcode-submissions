class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i != j, return the INDEX not values
        # Always a solution; can have negative values
        # Brute force approach: iterate over outside inner loop and check if nums[i] + nums[j] == target

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]