# https://leetcode.com/problems/contains-duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        remove_duplicates=set(nums)
        if len(nums)==len(remove_duplicates):
            return False
        else:
            return True

        