# 367. Valid Perfect Square
#
# Idea:
# - Binary search possible square roots from 0 to num.
# - If mid*mid == num -> True.
# - If mid*mid < num -> search right.
# - If mid*mid > num -> search left.
# - If loop ends without exact match -> False.
#
# Time: O(log n)
# Space: O(1)
class Solution(object):
    def isPerfectSquare(self, num):
        left=0
        right=num
        while left <= right:
            mid =(left+right)//2
            if mid*mid == num:
                return True 
            elif mid*mid < num:
                left=mid+1
            else:
                right=mid-1
        return False
