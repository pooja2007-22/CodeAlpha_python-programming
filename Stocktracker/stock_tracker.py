# Stock price dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800
}

total = 0

# Take input from user
for i in range(3):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found")

# Display result
print("Total Investment:", total)

# Save to file 
with open("result.txt", "w") as f:
    f.write(f"Total Investment: {total}")