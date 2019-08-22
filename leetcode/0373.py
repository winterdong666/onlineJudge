import queue

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        class helper:
            def __init__(self, s , pairs):
                self.sum = s
                self.pairs = pairs
            def __lt__(self, other):
                return self.sum > other.sum
        heap = queue.PriorityQueue()
        count = 0
        cando = True
        for i in range(len(nums1)):
            if cando:
                for j in range(len(nums2)):
                    if count < k:
                        heap.put(helper(nums1[i] + nums2[j], [nums1[i], nums2[j]]))
                        count += 1
                    else:
                        t = heap.get()
                        if nums1[i] + nums2[j] < t.sum:
                            heap.put(helper(nums1[i] + nums2[j], [nums1[i], nums2[j]]))
                        else:
                            heap.put(t)
                            if j == 0:
                                cando = False
                            break
            else:
                break
        res = []
        for i in range(heap.qsize()):
            t = heap.get()
            res.append(t.pairs)
        return res[::-1]
