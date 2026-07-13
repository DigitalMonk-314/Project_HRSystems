class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Position:
    def __init__ (self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary


class Employee:
    def __init__(self, id, name, age, department_id, position_id):
        self.id = id
        self.name = name
        self.age = age
        self.department_id = department_id
        self.position_id = position_id
    

class Project:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class EmployeeProject:
    def __init__(self, employee_id, project_id):
        self.employee_id = employee_id
        self.project_id = project_id