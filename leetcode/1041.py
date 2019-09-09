class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        index = [0, 0]
        state = 0
        for i in instructions:
            if i == "L":
                state += 1
                if state >= 4:
                    state = 0
            elif i == "R":
                state -= 1
                if state < 0:
                    state = 3
            else:
                if state == 0:
                    index[1] += 1
                elif state == 1:
                    index[0] -= 1
                elif state == 2:
                    index[1] -= 1
                elif state == 3:
                    index[0] += 1
        if (index[0] != 0 or index[1] != 0) and state == 0:
            return False
        else:
            return True
