import sqlite3
DB_PATH = "db/hr_system.db"

class DatabaseManager:
    """Класс отвечающий за создание таблиц"""
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def create_tables(self): 
        # Создание таблицы Departments
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL            
                );
                
        """)
        # Создание таблицы Positions
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS positions (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary INTEGER NOT NULL    
                );

        """)
        # Создание таблицы Employees
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                department_id INTEGER,
                position_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id),
                FOREIGN KEY (position_id) REFERENCES positions(id)  
                );

        """)
        # Создание таблицы Projects
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
                );

        """)
        # Создание таблицы EmployeeProjects
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee_projects (
                employee_id INTEGER,
                project_id INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees(id),
                FOREIGN KEY (project_id) REFERENCES projects(id) 
                );

        """)

        self.conn.commit()

    # CRUD Departments
    def add_department(self, name): # Добавляет новый отдел
        self.cursor.execute(
            "INSERT INTO departments (name) VALUES (?)",
            (name,)
        )
        self.conn.commit()

    def get_department(self, department_id): # Получает один отдел по ID
        self.cursor.execute(
            "SELECT id, name FROM departments WHERE id = ?",
            (department_id,)
        )
        return self.cursor.fetchone()
        
    
    def get_all_departments(self): # Получает список всех отделов
        self.cursor.execute("SELECT id, name FROM departments")
        return self.cursor.fetchall()
    
    def update_department(self, department_id, new_name): # Обновляет название отдела
        self.cursor.execute("UPDATE departments SET name = ? WHERE id = ?",
            (new_name, department_id)
        )
        self.conn.commit()

    def delete_department(self, department_id): # Удаляет отдел по ID
        self.cursor.execute("DELETE FROM departments WHERE id = ?",
            (department_id,)
        )
        self.conn.commit()

    # CRUD Positions
    def add_position(self, department_id, name, salary): # Добавляет новую должность
        self.cursor.execute("INSERT INTO positions (name, salary) VALUES (?, ?)",
            (name, salary)
        )
        self.conn.commit()

    def get_position(self, position_id): # Получает одну должность по ID --> изменил get_positions на get_position
        self.cursor.execute("SELECT id, name, salary FROM positions WHERE id = ?",
        (position_id,)
        )
        return self.cursor.fetchone()
    
    def get_all_positions(self): # Получает все должности
        self.cursor.execute("SELECT id, name, salary FROM positions")
        return self.cursor.fetchall()
    
    def update_position(self, position_id, name, salary, department_id=None): # Обновляет должность
        self.cursor.execute(
            "UPDATE positions SET name = ?, salary = ? WHERE id = ?",
            (name, salary, position_id)
        )
        self.conn.commit()

    def delete_position(self, position_id): # Удаляет должность
        self.cursor.execute(
            "DELETE FROM positions WHERE id = ?",
            (position_id,)
        )
        self.conn.commit()

    # CRUD Employees
    def add_employee(self, name, age, department_id, position_id): # Добавляет нового сотрудника
        self.cursor.execute(
            "INSERT INTO employees (name, age, department_id, position_id) VALUES (?, ?, ?, ?)",
            (name, age, department_id, position_id)
        )
        self.conn.commit()

    def get_employee(self, employee_id): # Получает одного сотрудника по ID
        self.cursor.execute(
            "SELECT id, name, age, department_id, position_id FROM employees WHERE id = ?",
            (employee_id,)
        )
        return self.cursor.fetchone()
    
    def get_all_employees(self): # Получает всех сотрудников
        self.cursor.execute("SELECT id, name, age, department_id, position_id FROM employees")
        return self.cursor.fetchall()

    def update_employee(self, employee_id, name, age, department_id, position_id): # Обновляет данные сотрудника
        self.cursor.execute(
            "UPDATE employees SET name = ?, age = ?, department_id = ?, position_id = ? WHERE id = ?",
            (name, age, department_id, position_id, employee_id)
        )
        self.conn.commit()

    def delete_employee(self, employee_id): # Удаляет сотрудника
        self.cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,)
        )
        self.conn.commit()

    #CRUD Projects
    def add_project(self, name, description): # Создает новый проект
        self.cursor.execute(
            "INSERT INTO projects (name, description) VALUES (?, ?)",
            (name, description)
        )
        self.conn.commit()
    
    def get_project(self, project_id): # Получает проект по ID
        self.cursor.execute(
            "SELECT id, name, description FROM projects WHERE id = ?",
            (project_id,)
        )
        return self.cursor.fetchone()
    
    def get_all_projects(self): # Получает все проекты
        self.cursor.execute("SELECT id, name, description FROM projects")
        return self.cursor.fetchall()
    
    def update_project(self, project_id, name, description): # Обновляет проект
        self.cursor.execute(
            "UPDATE projects SET name = ?, description = ? WHERE id = ?",
            (name, description, project_id)
        )
        self.conn.commit()

    def delete_project(self, project_id): # Удаляет проект
        self.cursor.execute(
            "DELETE FROM projects WHERE id = ?",
            (project_id,)
        )
        self.conn.commit()

    # CRUD EmployeeProjects
    def assign_employee_to_project(self, employee_id, project_id): # Назначает сотрудника на проект
        self.cursor.execute(
            "INSERT INTO employee_projects (employee_id, project_id) VALUES (?, ?)",
            (employee_id, project_id)
        )
        self.conn.commit()
    
    def remove_employee_from_project(self, employee_id, project_id): # Убирает сотрудника из проекта
        self.cursor.execute(
            "DELETE FROM employee_projects WHERE employee_id = ? AND project_id = ?",
            (employee_id, project_id)
        )
        self.conn.commit()

    def get_projects_from_employee(self, employee_id): # Получает проекты сотрудника
        self.cursor.execute(
            "SELECT project_id FROM employee_projects WHERE employee_id = ?",
            (employee_id,)
        )
        return self.cursor.fetchall()
    
    def get_employees_for_projects(self, project_id): # Получает сотрудников проекта (альтернативный метод)
        self.cursor.execute(
            "SELECT employee_id FROM employee_projects WHERE project_id = ?",
            (project_id,)
        )
        return self.cursor.fetchall()
    
    # Новые методы
    def get_positions_by_department(self, department_id): # Получает должности отдела
        self.cursor.execute(
            "SELECT id, name, salary FROM positions"
        )
        return self.cursor.fetchall()
    
    def get_employees_by_department(self, department_id): # Получает сотрудников отдела
        self.cursor.execute( 
            "SELECT id, name, age, position_id FROM employees WHERE department_id = ?",
            (department_id,)
        )
        return self.cursor.fetchall()
    
    def get_employees_by_position(self, position_id): # Получает сотрудников на должности
        self.cursor.execute(
            "SELECT id, name, age, department_id FROM employees WHERE position_id = ?"
        )
        return self.cursor.fetchall()
    
    def get_employees_in_project(self, project_id): # Получает сотрудников проекта
        self.cursor.execute(
            "SELECT employee_id FROM employee_projects WHERE project_id = ?",
            (project_id,)
        )
        return self.cursor.fetchall()   

    


