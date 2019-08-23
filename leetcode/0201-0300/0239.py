class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        monoQ = []
        head = 0
        for i in range(len(nums)):
            if len(monoQ) == head:
                monoQ.append(i)
            else:
                while len(monoQ) > head and nums[monoQ[-1]] < nums[i]:
                    monoQ.pop()
                monoQ.append(i)
                if monoQ[head] + k <= i:
                    head += 1
            res.append(nums[monoQ[head]])
        return res[k - 1:]
