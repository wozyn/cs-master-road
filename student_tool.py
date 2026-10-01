from student_utils import read_students_csv, calculate_average, save_json


data = read_students_csv("students.csv")

if data is not None:
    average = calculate_average(data)

    result = {
        "students": data,
        "average": average
    }

    save_json(result, "summary.json")

    print(result)