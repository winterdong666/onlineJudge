class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        total = 0
        for i in answers:
            count[i] = count.get(i, 0) + 1
        for i in count.keys():
            total += (i + 1) * ((count[i] - 1) // (i + 1) + 1)
        return total
