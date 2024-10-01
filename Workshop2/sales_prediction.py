# Anual profit 23% of top sales

projected = int(input("Enter projected amount of total sales: £"))

print(f"Profit made: £{(projected / 100) * .23}")

totalSales = .23

for year in range(1, 11):
    totalSales += 5
    print(f"Profit for year {year}: £{round((projected / 100) * totalSales)}")
