class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        neg_inf = -10**18
        dp = [[[neg_inf] * 3 for _ in range(m)] for _ in range(n)]

        dp[0][0][2] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                x = coins[i][j]

                for k in range(3):

                    if i > 0 and dp[i - 1][j][k] != neg_inf:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + x)

                    if j > 0 and dp[i][j - 1][k] != neg_inf:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + x)

                    if x < 0 and k < 2:
                        if i > 0 and dp[i - 1][j][k + 1] != neg_inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])

                        if j > 0 and dp[i][j - 1][k + 1] != neg_inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k + 1])

        return max(dp[n - 1][m - 1])