class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]>prices[i]:
        #             difference=prices[j]-prices[i]
        #             if difference>profit:
        #                 profit=difference
        # return profit

        # Note : Time limit exceeded for high input

        #Another Method

        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]-buy>profit:
                profit=prices[i]-buy
        return profit

        