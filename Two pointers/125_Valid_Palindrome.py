"""
LeetCode 125 - Valid Palindrome

Difficulty:
Easy

Concept:
Two Pointers

Problem:
Return True if the string is a palindrome after ignoring
non-alphanumeric characters and case.

Approach:
1. Use two pointers from both ends.
2. Skip non-alphanumeric characters.
3. Compare lowercase characters.
4. If all characters match, return True.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern Learned:
Two Pointers
"""

class Solution(object):
    def isPalindrome(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
