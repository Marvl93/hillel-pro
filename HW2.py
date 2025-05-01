students: list[dict] = []

def main():
    while True:
        print("\nОберіть дію:")
        print("1. Показати всіх студентів")
        print("2. Показати студента за ID")
        print("3. Додати нового студента")
        print("4. Вийти")

        choice = input("> ")

        if choice == '1':
            show_students()
        elif choice == '2':
            student_id_str = input("Введіть ID студента: ")
            try:
                student_id = int(student_id_str)
                show_student(student_id)
            except ValueError:
                print("Будь ласка, введіть ціле число для ID.")
        elif choice == '3':
            name = input("Введіть ім'я студента: ")
            marks_str = input("Введіть оцінки студента через кому (наприклад, 10,11,9): ")
            details = input("Введіть додаткову інформацію (необов'язково): ")
            try:
                marks = [int(mark.strip()) for mark in marks_str.split(',')]
                add_student(name, marks, details)
            except ValueError:
                print("Будь ласка, введіть оцінки у правильному форматі (числа, розділені комами).")
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

def show_students():
    if not students:
        print("Список студентів порожній.")
        return
    print("\nСписок студентів:")
    for student in students:
        print(f"ID: {student['id']}, Ім'я: {student['name']}, Оцінки: {student['marks']}")

def show_student(student_id: int):
    for student in students:
        if student['id'] == student_id:
            print(f"\nІнформація про студента з ID {student_id}:")
            print(f"ID: {student['id']}")
            print(f"Ім'я: {student['name']}")
            print(f"Оцінки: {student['marks']}")
            print(f"Додаткова інформація: {student['info']}")
            return
    print(f"Студента з ID {student_id} не знайдено.")

def add_student(name: str, marks: list[int], details: str | None):
    global students
    new_id = 1
    if students:
        new_id = students[-1]['id'] + 1
    new_student = {
        'id': new_id,
        'name': name,
        'marks': marks,
        'info': details if details is not None else ""
    }
    students.append(new_student)
    print(f"ID: {new_id} Додано студента '{name}', з оцінками: {marks} .")


if __name__ == "__main__":
    main()