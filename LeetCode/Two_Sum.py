# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict={}
        for index in range(len(nums)):
            if target-nums[index] not in nums_dict:
                nums_dict[nums[index]]=index
            else:
                return [nums_dict[target-nums[index]],index]