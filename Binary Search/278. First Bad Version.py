# ---------------------------------------------------------
# 278. First Bad Version
#
# Idea:
# - Use Binary Search on version numbers (1 to n).
# - Use the given API: isBadVersion(version).
# - If mid is bad:
#     Search the left half because there may be an earlier bad version.
# - If mid is good:
#     Search the right half.
# - When the loop ends:
#     left points to the first bad version.
#
# Time Complexity : O(log n)
# Space Complexity: O(1)
# ---------------------------------------------------------
class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) :
                right=mid-1
            else:
                left=mid+1
        return left
