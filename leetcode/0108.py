# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        def helper(nums, l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = helper(nums, l, m - 1)
            root.right = helper(nums, m + 1, r)
            return root
        return helper(nums, 0, len(nums) - 1)
