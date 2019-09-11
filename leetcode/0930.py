class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = 0
        if S == 0:
            l = 0
            while l < len(A):
                r = l
                while r < len(A) and A[r] == 0:
                    r += 1
                t = r - l
                count += (t * (t + 1) // 2)
                l = r + 1
            return count
        else:
            ones = []
            for i in range(len(A)):
                if A[i] == 1:
                    ones.append(i)
            if len(ones) < S:
                return count
            elif len(ones) == S:
                return (ones[0] + 1) * (len(A) - ones[-1])
            for i in range(len(ones) - S + 1):
                if i == 0:
                    count += (ones[i] + 1) * (ones[i + S] - ones[i + S - 1])
                elif i == len(ones) - S:
                    count += (ones[i] - ones[i - 1]) * (len(A) - ones[-1])
                else:
                    count += (ones[i] - ones[i - 1]) * (ones[i + S] - ones[i + S - 1])
            return count
                    
