# 374. Guess Number Higher or Lower
#
# Idea:
# - Binary search from 1 to n.
# - Use guess(mid):
#     0  -> Found the number.
#     1  -> Secret number is higher -> move left.
#    -1  -> Secret number is lower -> move right.
#
# Time Complexity : O(log n)
# Space Complexity: O(1)
class Solution(object):
    def guessNumber(self, n):
        left =1
        right=n
        while left <= right:
            mid=(left+right)//2
            result=guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                left=mid+1
            elif result == -1:
                right=mid-1
            
