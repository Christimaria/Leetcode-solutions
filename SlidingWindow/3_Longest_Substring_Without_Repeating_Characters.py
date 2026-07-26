"""
------------------------------------------------------------
LeetCode 3 - Longest Substring Without Repeating Characters

Difficulty:
Medium

Pattern:
Sliding Window + Hash Set

------------------------------------------------------------
Function Signature

def lengthOfLongestSubstring(self, s)

self
- Refers to the Solution object.
- Automatically created by LeetCode.

s
- Input string.

Example:
s = "abcabcbb"

LeetCode calls:

Solution().lengthOfLongestSubstring("abcabcbb")

Return:
The length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3

------------------------------------------------------------
Approach

1. Use two pointers (left and right) to represent the current window.
2. Use a Hash Set to store characters currently inside the window.
3. Expand the window by moving the right pointer.
4. If a duplicate character appears, remove characters from the left
   until the duplicate is removed.
5. Update the maximum window length.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern Learned:
Sliding Window

Key Formula:
Window Length = right - left + 1

------------------------------------------------------------
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            # Remove characters until duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len

"""
------------------------------------------------------------
Revision Notes

Pattern:
Sliding Window

When to Use:
- Longest substring
- Shortest substring
- Continuous subarray
- Maximum/Minimum window

Key Idea:
- Right pointer expands the window.
- Left pointer shrinks the window.
- Store current window elements in a Hash Set.
- Remove from the left until the window becomes valid.

Remember:
Window Length = right - left + 1

Interview Tip:
Whenever you see words like
"longest", "shortest", "continuous",
or "substring", think about the
Sliding Window technique.

Difficulty:
⭐⭐⭐ Medium

------------------------------------------------------------
"""
