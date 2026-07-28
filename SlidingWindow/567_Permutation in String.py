"""
LeetCode 567. Permutation in String

Pattern:
Fixed Size Sliding Window

Idea:
A permutation of s1 will have exactly the same character frequencies
as a substring of s2.

1. Store the frequency of characters in s1.
2. Maintain a sliding window of size len(s1) in s2.
3. Add the current character to the window.
4. If the window becomes larger than len(s1),
   remove the leftmost character and move the left pointer.
5. Compare the window frequency with s1's frequency.
6. If they are equal, a permutation exists.

Time Complexity:
O(n)

Space Complexity:
O(1)
(Only lowercase English letters)
"""


class Solution(object):
    def checkInclusion(self, s1, s2):

        # If s1 is longer, permutation is impossible
        if len(s1) > len(s2):
            return False

        # Frequency of characters in s1
        freq1 = {}

        # Frequency of characters in current window
        window = {}

        # Build frequency dictionary for s1
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        left = 0

        # Traverse s2
        for right in range(len(s2)):

            # Add current character to the window
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Shrink window if its size becomes greater than len(s1)
            if (right - left + 1) > len(s1):

                window[s2[left]] -= 1

                # Remove character if its count becomes zero
                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # Compare both frequency dictionaries
            if window == freq1:
                return True

        return False
