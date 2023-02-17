class Solution:
    # solution 1 O(n²)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums) - 1):
            for n2 in range(n + 1, len(nums)):
                sum = nums[n] + nums[n2]
                if sum == target:
                    return [n, n2]

    # solution 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
