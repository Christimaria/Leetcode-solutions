"""
LeetCode 76. Minimum Window Substring

Pattern:
Variable Size Sliding Window

Idea:
Find the smallest substring in s that contains all characters of t.

1. Store the frequency of characters in t.
2. Expand the window by moving the right pointer.
3. Track how many required characters are fully satisfied.
4. Once all required characters are present, shrink the window
   from the left while it remains valid.
5. Update the minimum window whenever a smaller valid window is found.

Time Complexity:
O(n)

Space Complexity:
O(m)
where m is the number of unique characters in t.
"""


class Solution(object):
    def minWindow(self, s, t):

        # Edge case
        if len(t) > len(s):
            return ""

        freqT = {}
        window = {}

        # Build frequency dictionary of t
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        need = len(freqT)
        have = 0

        left = 0

        minLength = float("inf")
        start = 0

        # Expand window
        for right in range(len(s)):

            window[s[right]] = window.get(s[right], 0) + 1

            # Check if current character's required frequency is satisfied
            if s[right] in freqT and window[s[right]] == freqT[s[right]]:
                have += 1

            # Shrink window while it is valid
            while have == need:

                windowLength = right - left + 1

                # Update smallest window
                if windowLength < minLength:
                    minLength = windowLength
                    start = left

                # Remove leftmost character
                window[s[left]] -= 1

                # Window becomes invalid
                if s[left] in freqT and window[s[left]] < freqT[s[left]]:
                    have -= 1

                left += 1

        if minLength == float("inf"):
            return ""

        return s[start:start + minLength]
