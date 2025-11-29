daily_sales = [5, 10, 12, 7, 3, 89, 15]

total_cups = sum(sales for sales in daily_sales if sales > 10)

print(total_cups)