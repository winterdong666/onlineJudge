class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        dicS = [0] * 10
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                A += 1
            else:
                dicS[int(secret[i])] += 1
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                B += (dicS[int(guess[i])] > 0)
                dicS[int(guess[i])] -= 1
        return str(A) + "A" + str(B) + "B"
