from pathlib import Path

if __package__:
    from .product_utils import read_products, calculate_total_value, save_summary
else:
    from product_utils import read_products, calculate_total_value, save_summary

BASE_DIR = Path(__file__).resolve().parent


if __name__ == "__main__":
    data = read_products(BASE_DIR / "products.csv")

    total = calculate_total_value(data)

    save_summary(data, total, BASE_DIR / "summary.json")

    print(data)
    print(total)