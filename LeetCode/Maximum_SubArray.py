# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        current_sum=0
        for index in range(len(nums)):
            current_sum=max(current_sum+nums[index],nums[index])
            max_sum=max(max_sum,current_sum)
        
        return max_sum