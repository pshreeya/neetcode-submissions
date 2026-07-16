class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buy day
        r = 1 #sell day

        max_profit = 0

        while r < len(prices):
            #is it profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                #we found a day with an even lower price! 
                #shift our buy day to this new low point
                l = r
            
            #always move the sell day forward to check the next price
            r += 1
            
        return max_profit



        