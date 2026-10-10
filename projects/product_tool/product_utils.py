import csv
import json


def read_products(filename):
    products = {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            # 跳过表头
            next(reader, None)

            for row in reader:
                try:
                    name = row[0].strip()

                    if name == "":
                        continue

                    price = float(row[1])
                    stock = int(row[2])

                except (ValueError, IndexError):
                    continue

                if price < 0 or stock < 0:
                    continue

                products[name] = {
                    "price": price,
                    "stock": stock
                }

    except FileNotFoundError:
        print("文件不存在")
        return None

    return products


def calculate_total_value(data):
    total_value = 0

    for product in data.values():
        total_value += product["price"] * product["stock"]

    return total_value


def save_summary(data, total, filename):

    summary = {
        "products": data,
        "total_value": total
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            summary,
            f,
            ensure_ascii=False,
            indent=4
        )