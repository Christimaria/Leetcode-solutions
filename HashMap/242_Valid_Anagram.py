"""
LeetCode 242 - Valid Anagram

Pattern:
Hash Map (Frequency Counting)

------------------------------------------------------------
Function Signature

def isAnagram(self, s, t)

self
- Refers to the Solution object.
- Automatically created by LeetCode.

s
- First input string.

Example:
s = "anagram"

t
- Second input string.

Example:
t = "nagaram"

LeetCode calls:

Solution().isAnagram("anagram", "nagaram")

Return:
True if both strings are anagrams.
False otherwise.

------------------------------------------------------------
Approach

1. If lengths differ, return False.
2. Count character frequencies for both strings.
3. Compare both dictionaries.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern Learned:
Frequency Counting using Hash Map

------------------------------------------------------------
"""

class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for ch in s:
            if ch in count_s:
                count_s[ch] += 1
            else:
                count_s[ch] = 1

        for ch in t:
            if ch in count_t:
                count_t[ch] += 1
            else:
                count_t[ch] = 1

        return count_s == count_t
