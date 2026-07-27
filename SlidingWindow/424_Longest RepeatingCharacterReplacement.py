"""
LeetCode 424. Longest Repeating Character Replacement

Pattern:
Sliding Window

Idea:
Maintain a sliding window and track the frequency of characters
inside the current window.

The number of replacements needed is:

window_length - max_frequency

If replacements needed > k,
shrink the window from the left.

Otherwise, update the maximum valid window length.

Steps
Expand the window using right.
Count character frequencies.
Track the maximum occurring character.
Check if the window is valid.
If invalid, move left.
Update the answer.

Time Complexity:
O(n)

Space Complexity:
O(1)
(Only 26 uppercase English letters)
"""


class Solution(object):
    def characterReplacement(self, s, k):

        # Left pointer of sliding window
        left = 0

        # Stores frequency of characters in current window
        freq = {}

        # Highest frequency character inside current window
        maxFreq = 0

        # Length of longest valid window
        maxLength = 0

        # Expand window
        for right in range(len(s)):

            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update maximum occurring character count
            maxFreq = max(maxFreq, freq[s[right]])

            # Current window size
            windowLength = right - left + 1

            # Shrink window if more than k replacements are needed
            while windowLength - maxFreq > k:

                freq[s[left]] -= 1
                left += 1

                windowLength = right - left + 1

            # Store longest valid window
            maxLength = max(maxLength, windowLength)

        return maxLength
