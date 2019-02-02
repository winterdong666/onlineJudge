class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxH = 0
        for i in range(len(height)):
            maxH = max(maxH, height[i])
        
        volume = maxH * len(height)
        for i in height:
            volume -= i
        currentH = 1
        for i in range(len(height)):
            while height[i] >= currentH:
                volume -= i
                currentH += 1
            if currentH > maxH:
                break
        currentH = 1
        for i in range(len(height) - 1, -1, -1):
            while height[i] >= currentH:
                volume -= (len(height) - 1 - i)
                currentH += 1
            if currentH > maxH:
                break
        return volume
