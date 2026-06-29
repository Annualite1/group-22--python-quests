# Known quantities and prices
scale_count = 3
scale_price = 10

tear_count = 5
tear_price = 3

# Calculate subtotal for each item, then add them together
scales_cost = scale_count * scale_price
tears_cost = tear_count * tear_price
total_cost = scales_cost + tears_cost

print(f"The total cost is {total_cost} gold.")