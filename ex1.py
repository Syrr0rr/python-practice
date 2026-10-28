prices = [25.00, 50.00, 75.00, 100.00, 150.00]
taxed_prices = list(map(lambda price: price * 0.80, prices))
rounded_taxed = list(map(lambda price: f"{price:.2f}", taxed_prices))
print(taxed_prices)
print(rounded_taxed)