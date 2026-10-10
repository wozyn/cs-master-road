import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
def read_products(filename):
    products = {}
    try:
        with open(filename,"r",encoding="utf-8")as f:
            reader = csv.reader(f)
            next(reader,None)
            for row in reader:
                name = row[0].strip()
                if name == "":
                    continue
                try:
                    price = float(row[1])
                    stock = int(row[2])
                except (ValueError,IndexError):
                    continue
                if price < 0 or stock < 0:
                    continue
                products[name] = {"price": price,"stock": stock}
    except FileNotFoundError:
        print("文件不存在")
        return None
    return products
data = read_products(BASE_DIR / "products.csv")
print(data)

def calculate_total_value(data):
    total_value=0
    for product in data.values():
        total_value += product["price"] * product["stock"]
    return total_value
    
data = read_products(BASE_DIR / "products.csv")

total = calculate_total_value(data)

print(total)
def save_summary(data, total, filename):
    summary = {
    "products": data,
    "total_value": total
    }
    with open(filename,"w",encoding="utf-8")as f:
        json.dump(summary,f,ensure_ascii=False,indent=4)


data = read_products(BASE_DIR / "products.csv")

total = calculate_total_value(data)

save_summary(data, total, BASE_DIR / "summary.json")
