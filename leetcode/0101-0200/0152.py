class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def Product(nums, l, r):
            if l > r:
                return -2147483647
            count = 1
            for i in range(l, r + 1):
                count *= nums[i]
            return count
        
        def maxProductWithoutZero(nums, l, r, minus):
            if l > r:
                return -2147483647
            elif l == r:
                return nums[l]
            if len(minus) % 2 == 0:
                return Product(nums, l, r)
            else:
                return max(Product(nums, l, minus[0] - 1), Product(nums, minus[0] + 1, r),
                          Product(nums, l, minus[-1] - 1), Product(nums, minus[-1] + 1, r))
                
        minus = []
        zeros = []
        tmp = []
        res = -2147483647
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
                minus.append(tmp[:])
                tmp = []
            if nums[i] < 0:
                tmp.append(i)
        minus.append(tmp)
        if len(zeros) > 0:
            res = max(res, maxProductWithoutZero(nums, 0, zeros[0] - 1, minus[0]))
            res = max(res, maxProductWithoutZero(nums, zeros[-1] + 1, len(nums) - 1, minus[-1]))
            for i in range(len(zeros) - 1):
                res = max(res, maxProductWithoutZero(nums, zeros[i] + 1, zeros[i + 1] - 1, minus[i + 1]))
            return max(0, res)
        else:
            return maxProductWithoutZero(nums, 0, len(nums) - 1, minus[0])
