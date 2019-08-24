class Solution:
    def validIPAddress(self, IP: str) -> str:
        ls = IP.split(".")
        if len(ls) == 4:
            valid = True
            for i in ls:
                if len(i) > 1 and i[0] == "0":
                    valid = False
                    break
                if i.isdigit() == False:
                    valid = False
                    break
                t = int(i)
                if t < 0 or t > 255:
                    valid = False
                    break
            if valid:
                return "IPv4"
        ls = IP.split(":")
        if len(ls) == 8:
            valid = True
            validKey = "0123456789abcdefABCDEF"
            for i in ls:
                if len(i) > 4 or len(i) == 0:
                    valid = False
                    break
                for j in i:
                    if not (j in validKey):
                        valid = False
                        break
                if valid == False:
                    break
            if valid:
                return "IPv6"
        return "Neither"
