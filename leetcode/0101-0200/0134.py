class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l0 = len(gas)
        gas = gas + gas[:-1]
        cost = cost + cost[:-1]
        l = len(gas)
        s = 0
        e = 0
        current = gas[0] - cost[0]
        if l0 == 1:
            if current >= 0:
                return 0
            else:
                return -1
        for i in range(1, l):
            if current < 0:
                s = i
                e = i
                current = gas[i] - cost[i]
            else:
                current += (gas[i] - cost[i])
                e += 1
            if current >= 0 and e - s >= l0 - 1:
                return s
        return -1
