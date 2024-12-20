class Solution:
    def climbStairs(self, n: int)->int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Инициализируем первые два значения
        first = 1  # ways(1)
        second = 2  # ways(2)

        # Итеративно вычисляем количество способов для каждого следующего шага
        for i in range(3, n + 1):
            current = first + second
            print(f'summa {current} = {first}+{second}')
            first = second
            print(f'first = {first}')
            second = current
            print(f'second = {second}')

        return second

n = 5

print(Solution().climbStairs(n))