"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
# class Solution:
#     def maxProfit(self, prices):
#         profit = []
#         for i in range(len(prices)-1):
#             buy = prices[i]
#             sell = max(prices[i+1:])
#             profit.append(sell-buy)
#         profit_max = max(profit)
#
#         return max(profit_max, 0)
"""
暴力穷举超时
"""
class Solution:
    def maxProfit(self, prices):
        # 记录最低价格
        inf = int(1e9)

        min_price = inf
        max_profit = 0
        for i in prices:
            max_profit = max(i - min_price, max_profit)
            min_price = min(i, min_price)

nums = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(nums))
