class MaxDiff :
    def buyAndSellStock(self, prices):
        if prices is None or len(prices) < 2 :
            return 0

        result = 0
        minimum = float('inf')

        for i in range(len(prices)) :
            minimum = min(prices[i], minimum)
            result = max(result,prices[i]-minimum)

        return result

    def buyAndSellStockTwoTrades(self, prices ):
        bestTillI = []
        bestFromI = []

        result = 0
        minimum = float('inf')

        for i in range(len(prices)) :
            minimum = min(prices[i], minimum)
            result = max(result,prices[i]-minimum)
            bestTillI.append(result)

        result = 0
        maximum = float('-inf')

        for i in range(len(prices)-1,-1,-1) :
            maximum = max(prices[i], maximum)
            result = max(result,maximum- prices[i])
            bestFromI.append(result)

        result = 0

        for i in range(len(bestTillI)) :
            result = max(result,max(bestTillI[i] + bestFromI[i]))


        return result

    def buyAndSellStock2OnePass(self, prices: List[int]) -> int:
        result = 0

        for i in range(1,len(prices)) :
            price = prices[i]

            if price > prices[i-1] :
                result += price - prices[i-1]


        return result


    def buyAndSellStock2OnePass(self, prices: List[int]) -> int:
        result = 0

        for i in range(1,len(prices)) :
            price = prices[i]

            if price > prices[i-1] :
                result += price - prices[i-1]


        return result

    def buyAndSellStock2PeakValleyApproach(self, prices):
        result = 0
        peak = prices[0]
        valley = prices[1]
        i = 0
        while i < len(prices) :
            while i < len(prices) and prices[i] <= prices[i+1] :
                i += 1
            peak = prices[i]

            while i < len(prices) and prices[i] > prices[i+1] :
                i += 1
            valley = prices[i]

            result += peak - valley

        return result

