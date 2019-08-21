class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        left = [1] + [0] * (l - 1)
        right = [0] * (l - 1) + [1]
        res = 0
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        for i in range(l):
            res += max(left[i], right[i])
        return res
