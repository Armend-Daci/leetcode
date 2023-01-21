class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key, value in enumerate(nums):
            for newkey, newvalue in enumerate(nums):
                if key != newkey and value + newvalue == target:
                    new_list = [key,newkey]
                    return new_list