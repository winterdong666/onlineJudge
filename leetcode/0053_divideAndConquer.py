class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divideAndConquer(nums, l, r):
            if l > r:
                return -2147483647
            
            m = (l + r) // 2
            
            leftSum = 0
            tmp = 0
            for i in range(m - 1, l - 1, -1):
                tmp += nums[i]
                leftSum = max(leftSum, tmp)
            
            rightSum = 0
            tmp = 0
            for i in range(m + 1, r + 1):
                tmp += nums[i]
                rightSum = max(rightSum, tmp)
            
            leftHalf = divideAndConquer(nums, l, m - 1)
            rightHalf = divideAndConquer(nums, m + 1, r)
            
            return max(leftSum + nums[m] + rightSum, max(leftHalf, rightHalf))
        return divideAndConquer(nums, 0, len(nums) - 1)
