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
            details = input("Введіть додаткову інформацію (необов'язково): ")
            add_student(name, [], details)
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

def show_students():
    """Виводить інформацію про всіх студентів."""
    if not students:
        print("Список студентів порожній.")
        return
    print("\nСписок студентів:")
    for student in students:
        print(f"ID: {student['id']}, Ім'я: {student['name']}")

def show_student(student_id: int):
    """Виводить інформацію про студента за його ID."""
    for student in students:
        if student['id'] == student_id:
            print(f"\nІнформація про студента з ID {student_id}:")
            print(f"ID: {student['id']}")
            print(f"Ім'я: {student['name']}")
            print(f"Оцінки: {student['marks']}")
            print(f"Інформація: {student['info']}")
            return
    print(f"Студента з ID {student_id} не знайдено.")

def add_student(name: str, marks: list[int], details: str | None):
    """Додає нового студента до списку."""
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
    print(f"Студента '{name}' додано з ID {new_id}.")

if __name__ == "__main__":
    main()