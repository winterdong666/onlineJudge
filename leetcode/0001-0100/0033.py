class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_min_index(nums, l, r):
            if l >= r:
                return l
            if r - l == 1:
                if nums[r] > nums[l]:
                    return l
                else:
                    return r
            m = (l + r) // 2
            if nums[m] > nums[r]:
                return find_min_index(nums, m, r)
            else:
                return find_min_index(nums, l, m)
        
        min_index = find_min_index(nums, 0, len(nums) - 1)
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[(m + min_index) % len(nums)] == target:
                return (m + min_index) % len(nums)
            elif nums[(m + min_index) % len(nums)] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
        
