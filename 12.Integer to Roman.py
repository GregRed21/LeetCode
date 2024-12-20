class Solution:
    def intToRoman(self, num):
        romans = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1}
        res = ''
        for sym, val in romans.items():
            if num // val:
                count = num // val
                res += (sym * count)
                num = num % val
        return res


print(Solution().intToRoman(1994))
