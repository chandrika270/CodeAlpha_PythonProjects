# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 180,
    "MSFT": 420
}

stock = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    price = stock_prices[stock]
    total = price * quantity

    print("\nStock:", stock)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Total Investment: $", total)

else:
    print("Stock not available.")
