import milkrate

litres, fat, snf = 10, 3.5, 8.5
rate = milkrate.rate_per_litre(fat, snf)
amount = milkrate.payout(litres, fat, snf)
print("Rate per litre:", rate)
print("Payment amount:", amount)
