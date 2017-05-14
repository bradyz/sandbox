class Solution(object):
    def canIWin(self, max_choose, total):
        if max_choose * (max_choose + 1) // 2 < total:
            return False
        return can_force(total, 2 ** max_choose - 1, max_choose, dict())


def is_on(x, i):
    return x & (1 << i) > 0


def turn_off(x, i):
    return x & ~(1 << i)


def can_force(total, chosen, max_choose, memo):
    if chosen in memo:
        return memo[chosen]

    for i in range(max_choose):
        if is_on(chosen, i) and i + 1 >= total:
            memo[chosen] = True
            return True

    for i in range(max_choose):
        if not is_on(chosen, i):
            continue
        elif not can_force(total - (i + 1), turn_off(chosen, i), max_choose, memo):
            memo[chosen] = True
            return True

    memo[chosen] = False
    return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canIWin(10, 11))
    print(solution.canIWin(10, 1))
    print(solution.canIWin(10, 0))
    print(solution.canIWin(10, 40))
