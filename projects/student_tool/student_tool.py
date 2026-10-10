from pathlib import Path

if __package__:
    from .student_utils import read_students_csv, calculate_average, save_json
else:
    from student_utils import read_students_csv, calculate_average, save_json

BASE_DIR = Path(__file__).resolve().parent


def main():
    data = read_students_csv(BASE_DIR / "students.csv")

    if data is not None:
        average = calculate_average(data)
        result = {
            "students": data,
            "average": average
        }
        save_json(result, BASE_DIR / "summary.json")
        print(result)


if __name__ == "__main__":
    main()
