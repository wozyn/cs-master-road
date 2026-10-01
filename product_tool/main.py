from product_utils import *


data = read_products("products.csv")

total = calculate_total_value(data)

save_summary(data, total, "summary.json")

print(data)
print(total)