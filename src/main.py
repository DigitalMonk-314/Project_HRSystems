from db_manager import DatabaseManager
db = DatabaseManager()
db.create_tables()

def menu_departments():
    print("\n=== Меню отделов ===")
    print("1. Создать отдел")
    print("2. Показать отдел")
    print("3. Показать все отделы")
    print("4. Обновить отдел")
    print("5. Удалить отдел")
    print("0. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Название отдела: ")
        db.add_department(name)
        print("Отдел создан.")

    elif choice == "2":
        dep_id = int(input("ID отдела: "))
        print(db.get_department(dep_id))

    elif choice == "3":
        print(db.get_all_departments())

    elif choice == "4":
        dep_id = int(input("ID отдела: "))
        new_name = input("Новое название: ")
        db.update_department(dep_id, new_name)
        print("Отдел обновлен.")

    elif choice == "5":
        dep_id = int(input("ID отдела: "))
        db.delete_department(dep_id)
        print("Отдел удален.")


def menu_positions():
    print("\n=== Меню должностей ===")
    print("1. Создать должность")
    print("2. Показать должность")
    print("3. Показать все должности")
    print("4. Показать должности отдела")
    print("5. Обновить должность")
    print("6. Удалить должность")
    print("0. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        dep_id = int(input("ID отдела: "))
        name = input("Название должности: ")
        salary = float(input("Зарплата: "))
        db.add_position(dep_id, name, salary)
        print("Должность создана.")

    elif choice == "2":
        pos_id = int(input("ID должности: "))
        print(db.get_position(pos_id))

    elif choice == "3":
        print(db.get_all_positions())

    elif choice == "4":
        dep_id = int(input("ID отдела: "))
        print(db.get_positions_by_department(dep_id))

    elif choice == "5":
        pos_id = int(input("ID должности: "))
        new_name = input("Новое название: ")
        new_salary = float(input("Новая зарплата: "))
        new_dep_id = int(input("Новый ID отдела: "))
        db.update_position(pos_id, new_name, new_salary, new_dep_id)
        print("Должность обновлена.")

    elif choice == "6":
        pos_id = int(input("ID должности: "))
        db.delete_position(pos_id)
        print("Должность удалена.")


def menu_employees():
    print("\n=== Меню сотрудников ===")
    print("1. Создать сотрудника")
    print("2. Показать сотрудника")
    print("3. Показать всех сотрудников")
    print("4. Показать сотрудников отдела")
    print("5. Показать сотрудников должности")
    print("6. Обновить сотрудника")
    print("7. Удалить сотрудника")
    print("0. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        age = int(input("Возраст: "))
        dep_id = int(input("ID отдела: "))
        pos_id = int(input("ID должности: "))
        db.add_employee(name, age, dep_id, pos_id)
        print("Сотрудник создан.")

    elif choice == "2":
        emp_id = int(input("ID сотрудника: "))
        print(db.get_employee(emp_id))

    elif choice == "3":
        print(db.get_all_employees())

    elif choice == "4":
        dep_id = int(input("ID отдела: "))
        print(db.get_employees_by_department(dep_id))

    elif choice == "5":
        pos_id = int(input("ID должности: "))
        print(db.get_employees_by_position(pos_id))

    elif choice == "6":
        emp_id = int(input("ID сотрудника: "))
        new_name = input("Новое имя: ")
        new_age = int(input("Новый возраст: "))
        new_dep_id = int(input("Новый ID отдела: "))
        new_pos_id = int(input("Новый ID должности: "))
        db.update_employee(emp_id, new_name, new_age, new_dep_id, new_pos_id)
        print("Сотрудник обновлен.")

    elif choice == "7":
        emp_id = int(input("ID сотрудника: "))
        db.delete_employee(emp_id)
        print("Сотрудник удален.")


def menu_projects():
    print("\n=== Меню проектов ===")
    print("1. Создать проект")
    print("2. Показать проект")
    print("3. Показать все проекты")
    print("4. Обновить проект")
    print("5. Удалить проект")
    print("6. Добавить сотрудника в проект")
    print("7. Показать сотрудников проекта")
    print("0. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Название проекта: ")
        desc = input("Описание: ")
        db.add_project(name, desc)
        print("Проект создан.")

    elif choice == "2":
        proj_id = int(input("ID проекта: "))
        print(db.get_project(proj_id))

    elif choice == "3":
        print(db.get_all_projects())

    elif choice == "4":
        proj_id = int(input("ID проекта: "))
        new_name = input("Новое название: ")
        new_desc = input("Новое описание: ")
        db.update_project(proj_id, new_name, new_desc)
        print("Проект обновлен.")

    elif choice == "5":
        proj_id = int(input("ID проекта: "))
        db.delete_project(proj_id)
        print("Проект удален.")

    elif choice == "6":
        emp_id = int(input("ID сотрудника: "))
        proj_id = int(input("ID проекта: "))
        db.add_employee_to_project(emp_id, proj_id)
        print("Сотрудник добавлен в проект.")

    elif choice == "7":
        proj_id = int(input("ID проекта: "))
        print(db.get_employees_in_project(proj_id))


def main_menu():
    while True:
        print("\n=== HR SYSTEM ===")
        print("1. Отделы")
        print("2. Должности")
        print("3. Сотрудники")
        print("4. Проекты")
        print("0. Выход")

        choice = input("Выберите раздел: ")

        if choice == "1":
            menu_departments()
        elif choice == "2":
            menu_positions()
        elif choice == "3":
            menu_employees()
        elif choice == "4":
            menu_projects()
        elif choice == "0":
            print("Выход...")
            break


if __name__ == "__main__":
    main_menu()

   
