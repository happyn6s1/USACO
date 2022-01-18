class Solution:
    def maxProfit(prices):
        max=0
        highest=-99999999
        if len(prices)==0:
            return 0
        
        lowest=prices[0]
        for i in range(len(prices)):
            if prices[i] > highest:
                highest=prices[i]
            if prices[i] < lowest:
                lowest=prices[i]
                highest=lowest
            if highest-lowest>max:
                max=highest-lowest
        return max

prices=[7,1,5,3,6,4,23,12,52,1,122,1231]
print(Solution.maxProfit(prices))
