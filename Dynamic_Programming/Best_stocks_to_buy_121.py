'''
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a
#different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def max_profit(prices):
    sorted_prices = sorted(prices)
    length_of_prices = len(prices)
    #print(sorted_prices)
    #print(prices.index(7))
    maxProfit = 0
    if sorted_prices[0] == prices[length_of_prices-1]:

        return maxProfit
    else:
        index_of_min = prices.index(sorted_prices[0])
        for i in range(index_of_min+1,length_of_prices):
            profit = prices[i] - prices[index_of_min]
            if maxProfit < profit:
                maxProfit = profit
        return maxProfit

#Time complexity = O(n*n) + n
#Space complexity = O(n)
#print(max_profit([7,1,5,3,6,4]))
#print(max_profit([7,6,4,3,1]))

def better_solution(prices):
    maximum_profit, min_price = 0,float("inf") #Storing infinite in min_price, to find min value in array
    for price in prices:
        min_price = min(min_price,price)
        maximum_profit = max(maximum_profit, price-min_price)

    return maximum_profit

#Time complexity = O(n)
#Space complexity = O(1)
print(better_solution([7,1,5,3,6,4]))
print(better_solution([7,6,4,3,1]))
