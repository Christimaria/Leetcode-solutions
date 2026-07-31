"""
LeetCode 438. Find All Anagrams in a String

Pattern:
Fixed Size Sliding Window

Idea:
Maintain a window of size len(p) in s.

1. Store the frequency of characters in p.
2. Traverse s using a sliding window.
3. Add the current character to the window.
4. If the window becomes larger than len(p),
   remove the leftmost character.
5. Compare the window frequency with p's frequency.
6. If both are equal, append the starting index.

Key Observation

A substring is an anagram of p if both have the same character frequencies.
Instead of generating all permutations of p, compare the frequency dictionaries.

Time Complexity:
O(n)

Space Complexity:
O(1)
(Only lowercase English letters)
"""


class Solution(object):
    def findAnagrams(self, s, p):

        # Stores the answer
        result = []

        # Frequency of characters in p
        freqP = {}

        # Frequency of current window
        window = {}

        # Edge case
        if len(p) > len(s):
            return result

        # Build frequency dictionary of p
        for ch in p:
            freqP[ch] = freqP.get(ch, 0) + 1

        left = 0

        # Traverse s
        for right in range(len(s)):

            # Add current character
            window[s[right]] = window.get(s[right], 0) + 1

            # Keep window size equal to len(p)
            if (right - left + 1) > len(p):

                window[s[left]] -= 1

                # Remove key if count becomes zero
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # If current window is an anagram, store its starting index
            if window == freqP:
                result.append(left)

        return result

  '''
  Algorithm
Build the frequency dictionary of p.
Maintain a fixed-size sliding window of length len(p) in s.
Add one character as the window expands.
Remove one character when the window exceeds the required size.
Compare the window frequency with p's frequency.
If equal, store the starting index (left).
Return the list of all starting indices.'''
