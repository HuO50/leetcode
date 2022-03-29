
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

    # 双指针法
    def maxProfit4(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        for right in range(1, len(prices)):
            if (prices[left] > prices[right]):
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit

    def maxProfit5(self, prices: List[int]) -> int:
        left = 0
        right = len(prices) - 1
        max_profit = self.divideList(prices, left, right)
        return max_profit

    def divideList(self, prices, left, right):
        if left == right:
            return
        mid = (left + right) / 2
        divideList(prices, left, mid)
        divideList(prices, mid + 1, right)
        self.mergeList(prices, left, mid, right, res)

    def mergeList(self, prices, left, mid, right, res):
        max_price = float('-inf')
        min_price = float('inf')

        for i in range(left, mid):
            min_price = min(min_price, prices[i])

        for i in range(mid + 1, right)
        max_price = max(max_price, prices[i])

        ret = max_price - min_price
        if (res < ret):
            return ret
        else:
            return res


if __name__ == "__main__":
    asolute = Solution()
    result = asolute.maxProfit4([1, 2, 3])
    print(result)
