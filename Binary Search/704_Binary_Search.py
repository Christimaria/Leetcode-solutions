BINARY SEARCH
'''
Pattern:Binary Search

Time : O(log n)
Space: O(1)

Initialize:
left = 0
right = n-1

Remember:
• Array must be sorted
• while left <= right
• left = mid + 1
• right = mid - 1
'''
class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left <= right:

            mid=(left+right)//2
            if target ==nums[mid]:
                return mid
            elif target > nums[mid]:
                left=mid+1
            else :
                right=mid-1
        return -1



        
