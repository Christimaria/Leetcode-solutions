"""
LeetCode 242 - Valid Anagram

Difficulty:
Easy

Concept:
Hash Map (Dictionary)

Problem:
Return True if two strings are anagrams of each other.

Approach:
1. If lengths are different, return False.
2. Count the frequency of each character in both strings.
3. Compare both dictionaries.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern Learned:
Frequency Counting using Hash Map
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
