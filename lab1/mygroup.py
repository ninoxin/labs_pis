def average(marks):
    return sum(marks) / len(marks) if marks else 0.0

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(12), "Экзамены".ljust(35), "Оценки".ljust(15), "Средний".ljust(7))
    for s in students:
        avg = average(s["marks"])
        print(s["name"].ljust(15), s["surname"].ljust(12), str(s["exams"]).ljust(35), str(s["marks"]).ljust(15), ("{:.2f}".format(avg)).ljust(7))

def filter_by_average(students, threshold):
    return [s for s in students if average(s["marks"]) > threshold]

groupmates = [
    {"name": "Александр", "surname": "Иванов", "exams": ["Информатика", "ЭЭиС", "Web"], "marks": [4, 3, 5]},
    {"name": "Иван",      "surname": "Петров", "exams": ["История", "АиГ", "КТП"],   "marks": [4, 4, 4]},
    {"name": "Кирилл",    "surname": "Смирнов","exams": ["Философия", "ИС", "КТП"], "marks": [5, 5, 5]},
    {"name": "Мария",     "surname": "Кузнецова","exams":["Мат.анализ","Физика","АиГ"],"marks":[3,4,4]},
    {"name": "Ольга",     "surname": "Соколова","exams": ["Информатика","ИС","Web"], "marks":[5,4,4]},
    {"name": "Дмитрий",   "surname": "Васильев","exams": ["История","Философия","КТП"],"marks":[2,3,3]},
]

if __name__ == "__main__":

    user_in = input("Введите порог среднего балла (например, 4.0). Оставьте пустым для вывода всех: ").strip()
    if user_in == "":
        print("\nСписок всех студентов:\n")
        print_students(groupmates)
    else:
        try:
            threshold = float(user_in.replace(',', '.'))
        except ValueError:
            print("Ошибка ввода. Используйте число, например 4 или 4.0")
        else:
            filtered = filter_by_average(groupmates, threshold)
            print(f"\nСтуденты со средним баллом выше {threshold}:\n")
            if filtered:
                print_students(filtered)
            else:
                print("Нет студентов, удовлетворяющих условию.")