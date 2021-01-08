
from typing import List


class Solution:
    # 暴力法1
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        list_size = len(prices) + 1

        price_count = [[0 for i in range(list_size)] for j in range(list_size)]

        price_count[0][1:] = prices

        for i in range(0, len(prices)):
            price_count[i+1][0] = prices[i]

        max_profit = 0
        for i in range(1, list_size):
            for j in range(i+1, list_size):
                price_count[j][i] = price_count[j][0] - price_count[0][i]
                if price_count[j][i] > max_profit:
                    max_profit = price_count[j][i]
        return max_profit

    # 暴力法2
    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        count = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                count = count + 1
        if (count == len(prices)):
            return 0

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                tmp = prices[j] - prices[i]
                if (j == len(prices)) and max_profit is 0:
                    return 0
                if tmp > max_profit:
                    max_profit = tmp
        return max_profit

    # 动态规划1
    def maxProfit3(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprice = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprice = max(maxprice, price - minprice)
        return maxprice


if __name__ == "__main__":
    asolute = Solution()
    result = asolute.maxProfit3([1, 2, 3])
    print(result)
