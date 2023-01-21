class Solution:
    def intToRoman(self, num: int) -> str:
        new = ""
        if num / 1000 >= 1:
            new += int(num/1000) * "M"
            num = num % 1000
        if num / 900 >= 1:
            new += int(num/900) * "CM"
            num = num % 900
        if num / 500 >= 1:
            new += int(num/500) * "D"
            num = num % 500
        if num / 400 >= 1:
            new += int(num/400) * "CD"
            num = num % 400
        if num / 100 >= 1:
            new += int(num/100) * "C"
            num = num % 100
        if num / 90 >= 1:
            new += int(num/90) * "XC"
            num = num % 90
            print(num,new)
        if num / 50 >= 1:
            new += int(num/50) * "L"
            num = num % 50
        if num / 40 >= 1:
            new += int(num/40) * "XL"
            num = num % 40
        if num / 10 >= 1:
            new += int(num/10) * "X"
            num = num % 10
        if num / 9 >= 1:
            new += int(num/9) * "IX"
            num = num % 9
        if num / 5 >= 1:
            new += int(num/5) * "V"
            num = num % 5
        if num / 4 >= 1:
            new += int(num/4) * "IV"
            num = num % 4
        if num / 1 >= 1:
            new += int(num/1) * "I"
            num = num % 1
        return new