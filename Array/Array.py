#Stock Prices value for 5 days
#Day no:        1   2   3   4   5
stock_price = [205,852,369,445,999]

#What was the price on day 3?
print(stock_price[2])
#complexity: O(1)

#On what day price was 445?
for i in range(len(stock_price)):
    if stock_price[i] == 445:
        print(i+1)
#complexity: O(1)
    
#Print all prices
for i in stock_price:
    print(i)
#complexity: O(n)

#Insert new price 284 at index 1
stock_price.insert(1,284)
print(stock_price)
#complexity: O(n) [when we insert the value, after inserting the value of the given location it will shift all the elements by one position]

#Delete element at index 1
stock_price.pop(1)
print(stock_price)
#complexity: O(n)

#Delete 852 price from stock price
stock_price.remove(852) 
print(stock_price)
#complexity: O(n) 
