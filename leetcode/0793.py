class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        if K == 0:
            return 5
        base = [1]
        while base[-1] <= K:
            base.append(base[-1] * 5 + 1)
        base.pop()
        while len(base) > 0:
            if K // base[-1] == 5:
                return 0
            else:
                K = K % base[-1]
                base.pop()
        return 5
