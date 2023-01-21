class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        length = len(s)
        print(length)
        for key, value in enumerate(s):
            if value == "M":  # checks for 1000
                if key == 0 or s[key - 1] != "C":
                    total += 1000
                else:
                    pass
            elif value == "C" and length > key + 1 and s[key + 1] == "M":  # checks for 900
                total += 900
            elif value == "D":
                if key == 0 or s[key - 1] != "C":
                    total += 500
                else:
                    pass
            elif value == "C" and length > key + 1 and s[key + 1] == "D":
                total += 400
            elif value == "C":
                if key == 0 or s[key - 1] != "X":
                    total += 100
                else:
                    pass
            elif value == "X" and length > key + 1 and s[key + 1] == "C":
                total += 90
            elif value == "L":
                if key == 0 or s[key - 1] != "X":
                    total += 50
                else:
                    pass
            elif value == "X" and length > key + 1 and s[key + 1] == "L":
                total += 40
            elif value == "X":
                if key == 0 or s[key - 1] != "I":
                    total += 10
                else:
                    pass
            elif value == "I" and length > key + 1 and s[key + 1] == "X":
                total += 9
            elif value == "V":
                if key == 0 or s[key - 1] != "I":
                    total += 5
                else:
                    pass
            elif value == "I" and length > key + 1 and s[key + 1] == "V":
                total += 4
            elif value == "I":
                total += 1
        return total