import csv
import json

def read_students_csv(filename):
    data = {}

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            data[row[0]] = int(row[1])

    return data


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


data = read_students_csv("students.csv")
save_json(data, "students.json")

def read_students_csv(filename):
    data = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader,None)              
            for row in reader:
                try:
                    name = row[0].strip()
                    score = int(row[1])
                    if name == "":
                        print("姓名为空")
                        continue
                    if score < 0 or score > 100:
                        print("分数超出范围")
                        continue
                    data[name] = score
                except (ValueError,IndexError):
                    print("数据有误")
        return data
    except FileNotFoundError:
        print("找不到")

def calculate_average(data):
    total = 0
    if data=={}:
        return 0

    for score in data.values():
        total += score
    return total/len(data)


    

    
    
data = read_students_csv("students.csv")

if data is not None:
    average = calculate_average(data)

    result = {
        "students": data,
        "average": average
    }

    save_json(result, "summary.json")

    print(result)