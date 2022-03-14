# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Snippet for removing alphanumeric characters 
        # And converting uppercase letter to lowercase
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        
        if s==s[::-1]:
            return True
        else:
            return False