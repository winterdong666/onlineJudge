class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        items, counts = [], []
        for i in count.keys():
            items.append(i)
            counts.append(count[i])
        def subsetsHelper(items, counts):
            if counts == []:
                return [[]]
            res = subsetsHelper(items[1:], counts[1:])
            for i in range(len(res)):
                tmp = res[i][:]
                for j in range(counts[0]):
                    tmp.append(items[0])
                    res.append(tmp[:])
            return res
        return subsetsHelper(items, counts)
