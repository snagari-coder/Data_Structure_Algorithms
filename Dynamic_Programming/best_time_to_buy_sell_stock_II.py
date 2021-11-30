#Leetcode 121:
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution(object):
    import sys
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice,maxProfit = float('inf'),0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                
        return maxProfit
    #time = O(n)
###################################################
# Leetcode : 122
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit
     
 # Input: prices = [7,1,5,3,6,4]
 # Output: 7
  
 # Input: prices = [1,2,3,4,5]
 # Output: 4
  
 # Time complexity - O(n)
 # Space complexity - O(1)
  
