stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

stock_name = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))

price = stocks[stock_name]
total = price * quantity

print("Stock Name:", stock_name)
print("Stock Price:", price)
print("Quantity:", quantity)
print("Total Investment:", total)