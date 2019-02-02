class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def compare(left,right):
            if not left or not right:
                return True 
            return left[-1] <= right[0]

        def extremum(list1,list2,extreme_index,extreme_fun):
            if not list1:
                return list2[extreme_index]
            elif not list2:
                return list1[extreme_index]
            else:
                return extreme_fun(list1[extreme_index],list2[extreme_index])

        if len(nums1) > len(nums2):
            nums2,nums1 = nums1,nums2
        
        x, y = len(nums1), len(nums2)
        start, end = 0, x - 1

        while True:
            p1  = (start + end) // 2 + 1 #(start + end)//2 是搜索的中点坐标，+1获得个数意义
            p2  = (x + y + 1)//2 - p1
            if not compare(nums1[:p1],nums2[p2:]) :
                end = p1 - 2  #右界坐标变成中点坐标-1
            elif not compare(nums2[:p2],nums1[p1:]):
                start = p1    #左界左标变成中点坐标+1
            else:
                break

        leftmax = extremum(nums1[:p1],nums2[:p2],-1,max)
        if (x+y)%2 == 0:
            rightmin = extremum(nums1[p1:],nums2[p2:],0,min)
            return (leftmax + rightmin ) / 2
        else:
            return leftmax
