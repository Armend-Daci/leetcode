class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        while nums.count(nums[curr]) != 1:
            curr += 1
        return nums[curr]