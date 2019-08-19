class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getGCD(v1, v2):
            if v1 < v2:
                t = v1
                v1 = v2
                v2 = t
            if v1 % v2 == 0:
                return v2
            t = v1 % v2
            v11 = v2
            v21 = t
            return getGCD(v11, v21)
        def getSlope(p1 ,p2):
            if p1[0] == p2[0]:
                return "inf"
            if p1[1] == p2[1]:
                return "0"
            sign = 1
            v1 = p1[1] - p2[1]
            v2 = p1[0] - p2[0]
            if v1 < 0:
                v1 = -v1
                sign *= -1
            if v2 < 0:
                v2 = -v2
                sign *= -1
            gcd = getGCD(v1, v2)
            return (v1 / gcd, v2 / gcd, sign)
        if len(points) <= 2:
            return len(points)
        res = 0
        l = len(points)
        for i in range(l):
            dic = {}
            same = 0
            for j in range(l):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                    continue
                s = getSlope(points[i], points[j])
                dic[s] = dic.get(s, 0) + 1
            for t in dic.values():
                if res < t + same:
                    res = t + same
            res = max(res, same)
        return res
